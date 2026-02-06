# config.py

LLM_PROVIDER = "GPT4"  # or "CLAUDE3"

# Keep API key local (never hardcode in production)
OPENAI_API_KEY = "YOUR_API_KEY_HERE"

SUPPORTED_LANGUAGES = ["en", "hi"]

AUDIT_LOG_PATH = "audit_logs/logs.json"
TEMPLATE_PATH = "knowledge_base/templates.json"
