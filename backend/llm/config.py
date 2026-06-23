import os
from dotenv import load_dotenv

import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "gemini")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini")

load_dotenv()

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "gemini"
)

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3"
)