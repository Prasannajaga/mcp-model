import importlib

packages = [
    "aiohttp",
    "anthropic",
    "google.genai",
    "google.generativeai",
    "mcp",
    "openai",
    "dotenv",
]

for pkg in packages:
    try:
        importlib.import_module(pkg)
        print(f"✅ {pkg} is installed")
    except ModuleNotFoundError:
        print(f"❌ {pkg} is NOT installed")
