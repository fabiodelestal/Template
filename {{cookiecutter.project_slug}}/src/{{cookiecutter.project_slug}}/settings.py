"""Configuración del proyecto usando variables de entorno."""

import os
from pathlib import Path

from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()


class Settings:
    """Configuración centralizada del proyecto."""

    # Rutas
    BASE_DIR: Path = Path(__file__).parent.parent.parent
    LOGS_DIR: Path = BASE_DIR / "logs"

    # Configuración de la aplicación
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Añade aquí más variables de entorno


settings = Settings()
