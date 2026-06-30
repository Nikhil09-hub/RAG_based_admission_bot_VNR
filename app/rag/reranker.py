from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from pinecone import Pinecone

from app.config import get_settings

if TYPE_CHECKING:
    from app.rag.retriever import RetrievedChunk


logger = logging.getLogger(__name__)
settings = get_settings()

_pinecone_client: Pinecone | None = None


def _get_pinecone_client() -> Pinecone:
    global _pinecone_client

    if _pinecone_client is None:
        _pinecone_client = Pinecone(
            api_key=settings.PINECONE_API_KEY
        )

    return _pinecone_client


def rerank_chunks(
    query: str,
    chunks: list["RetrievedChunk"],
    top_n: int = 4,
) -> list["RetrievedChunk"]:
    """
    Receives Pinecone candidate chunks and returns only the most relevant chunks.
    Falls back to original Pinecone order if reranking fails.
    """
    if not chunks:
        return []

    documents = [
        {
            "id": str(index),
            "text": chunk.text,
        }
        for index, chunk in enumerate(chunks)
        if chunk.text.strip()
    ]

    if not documents:
        return chunks[:top_n]

    try:
        pc = _get_pinecone_client()

        result = pc.inference.rerank(
            model="bge-reranker-v2-m3",
            query=query,
            documents=documents,
            top_n=min(top_n, len(documents)),
            return_documents=True,
            parameters={
                "truncate": "END",
            },
        )

        reranked_chunks: list[RetrievedChunk] = []

        for item in result.data:
            original_index = item.index

            if original_index < 0 or original_index >= len(chunks):
                continue

            original_chunk = chunks[original_index]

            original_chunk.rerank_score = item.score
            reranked_chunks.append(original_chunk)

        if reranked_chunks:
            logger.info(
                "RERANK | candidates=%d | selected=%d",
                len(chunks),
                len(reranked_chunks),
            )
            for i, chunk in enumerate(reranked_chunks, 1):

                logger.info(
                    "RERANKED CHUNK %s | text=%s",
                    i,
                    chunk.text[:500],
                )
            return reranked_chunks

    except Exception as exc:
        logger.warning(
            "RERANK_FAILED | using Pinecone order | error=%s",
            exc,
        )

    return chunks[:top_n]