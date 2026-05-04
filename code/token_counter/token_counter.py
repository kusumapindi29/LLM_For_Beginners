import tiktoken

MODEL = "gpt-4o-mini"

def count_tokens(text: str) -> int:
    encoding = tiktoken.encoding_for_model(MODEL)
    return len(encoding.encode(text))

sample = """
FastAPI is commonly used for building AI APIs.
"""

tokens = count_tokens(sample)

print(f"Token count: {tokens}")
