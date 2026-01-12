# {{ cookiecutter.project_name }}

## Setup

```bash
uv sync --extra dev
uv run pre-commit install
```

## Commands

```bash
uv run python -m {{ cookiecutter.project_slug }}
uv run pytest
uv run ruff check . --fix
uv run ty check
```
