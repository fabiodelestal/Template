# Python Project Template

Template cookiecutter para proyectos Python con uv, ruff, ty y loguru.

## Uso

```bash
uvx cookiecutter https://github.com/fabiodelestal/Template.git
```

Te pedirá:
- `project_name`: Nombre del proyecto (ej: "Mi Proyecto")

## Después de generar

```bash
cd mi_proyecto
uv sync --extra dev
uv run pre-commit install
```

## Herramientas incluidas

- **uv** - Gestión de dependencias
- **ruff** - Linting + formatting
- **ty** - Type checking
- **pre-commit** - Hooks automáticos
- **loguru** - Logging
