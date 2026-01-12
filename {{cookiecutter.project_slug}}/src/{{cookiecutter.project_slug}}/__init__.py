"""{{ cookiecutter.project_name }}.

Este módulo configura el logging y exporta la versión del paquete.
"""

from loguru import logger

logger.add("logs/{time:YYYY-MM-DD}.log", rotation="1 day", retention="7 days")

__version__ = "0.1.0"
