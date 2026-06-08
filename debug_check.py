from app.api import chat as chat_api
q = 'Tell me about IT department'
print('is_cutoff_like_query:', chat_api._is_cutoff_like_query(q))
print('extract_cutoff_program_scope:', chat_api._extract_cutoff_program_scope(q))
try:
    print('extract_branch:', chat_api.extract_branch(q))
except Exception as e:
    print('extract_branch error:', e)
