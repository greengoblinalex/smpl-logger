import sys
import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler

LOG_CONFIG = {
    "LOG_DIR": Path("logs"),
    "LEVEL": "INFO",
    "FORMAT": "%(asctime)s | %(name)s | [%(levelname)s] | %(message)s",
    "DATE_FORMAT": "%Y-%m-%d %H:%M:%S",
    "ROTATION_SIZE": 5 * 1024 * 1024,  # 5 mb
    "BACKUP_COUNT": 3,
    "ENCODING": "utf-8",
}

LOG_CONFIG["LOG_DIR"].mkdir(parents=True, exist_ok=True)


class ColoredFormatter(logging.Formatter):
    """Форматтер с цветным выводом для консоли"""

    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "CRITICAL": "\033[41m",  # Red background
    }
    RESET = "\033[0m"

    def format(self, record):
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{self.RESET}"
        formatted = super().format(record)

        record.levelname = levelname
        return formatted


def get_logger(
    name: str,
    log_file: str = None,
    level: str = None,
    rotation_size: int = None,
    backup_count: int = None,
) -> logging.Logger:
    """Создает и настраивает логгер.

    Args:
        name: Имя логгера. Используя "root", вы настраиваете корневой логгер.
        log_file: Имя файла для записи логов. Если None, логи пишутся только в консоль.
        level: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL).
              По умолчанию используется значение из LOG_CONFIG["LEVEL"].
        rotation_size: Максимальный размер файла лога в байтах перед ротацией.
              По умолчанию используется значение из LOG_CONFIG["ROTATION_SIZE"].
        backup_count: Количество сохраняемых архивных файлов при ротации.
              По умолчанию используется значение из LOG_CONFIG["BACKUP_COUNT"].

    Returns:
        Настроенный объект Logger с обработчиками для консоли и файла (если указан).

    Notes:
        - Если логгер с указанным именем уже существует и имеет обработчики,
          возвращается существующий логгер без изменений.
        - Консольный вывод форматируется с цветовой подсветкой уровней логирования.
        - Файловый вывод (если указан) настраивается с ротацией по размеру.
    """
    logger = logging.getLogger(name)
    level = level or LOG_CONFIG["LEVEL"]
    logger.setLevel(getattr(logging, level.upper()))

    if logger.hasHandlers():
        return logger

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        ColoredFormatter(fmt=LOG_CONFIG["FORMAT"], datefmt=LOG_CONFIG["DATE_FORMAT"])
    )
    logger.addHandler(console_handler)

    if log_file:
        log_path = LOG_CONFIG["LOG_DIR"] / log_file
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_path,
            maxBytes=rotation_size or LOG_CONFIG["ROTATION_SIZE"],
            backupCount=backup_count or LOG_CONFIG["BACKUP_COUNT"],
            encoding=LOG_CONFIG["ENCODING"],
        )
        file_handler.setFormatter(
            logging.Formatter(
                fmt=LOG_CONFIG["FORMAT"], datefmt=LOG_CONFIG["DATE_FORMAT"]
            )
        )
        logger.addHandler(file_handler)

    return logger
