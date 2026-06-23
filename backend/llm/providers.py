from backend.llm.config import (
    LLM_PROVIDER,
    GEMINI_API_KEY,
    GEMINI_MODEL,
    OLLAMA_MODEL,
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL
)

from langchain_ollama import ChatOllama
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


def get_llm():
    provider = LLM_PROVIDER.lower()

    if provider == "ollama":
        return ChatOllama(
            model=OLLAMA_MODEL,
            temperature=0
        )

    if provider == "gemini":
        return ChatGoogleGenerativeAI(
            model=GEMINI_MODEL,
            google_api_key=GEMINI_API_KEY,
            temperature=0
        )

    if provider == "openrouter":
        return ChatOpenAI(
            model=OPENROUTER_MODEL,
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "agentic-career-platform"
            },
            temperature=0
        )

    raise ValueError(f"Unsupported provider: {provider}")