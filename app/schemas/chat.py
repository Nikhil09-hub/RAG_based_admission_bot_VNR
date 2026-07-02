from pydantic import BaseModel, Field

class ChatResponse(BaseModel):
    response: str
    intent: str = "informational"
    metadata: dict = Field(default_factory=dict)
    options: list[dict] = Field(default_factory=list)