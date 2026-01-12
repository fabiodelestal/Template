"""Punto de entrada principal de {{ cookiecutter.project_name }}."""

from loguru import logger

from {{ cookiecutter.project_slug }}.settings import settings


def main() -> None:
    """Ejecuta la aplicación principal."""
    logger.info(f"Starting {{ cookiecutter.project_name }} (DEBUG={settings.DEBUG})")


if __name__ == "__main__":
    main()
