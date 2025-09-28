# LionsFinancial/helpers/__init__.py
import sys
from loguru import logger

logger.remove(0)
logger.add(sys.stderr, format="{time:HH:mm:ss} | {level} | {message}", level="INFO")
logger.add(
    "logs/app.log",
    level="INFO",
    format="{time:HH:mm:ss} | {level} | {message}",
)

logger.info("logger has started")
