## 🔧 Setting Up the Environment (using uv)

```bash
# 1. Create and activate a virtual environment using uv
uv venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 2. Install all project dependencies from pyproject.toml
uv pip install -r requirements.txt  # or just:
uv pip install .

# 3. Run the application or scripts
uv run <file>
