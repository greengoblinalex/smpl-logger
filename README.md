# Simple Logger

Простая библиотека для логирования с цветным форматированием и поддержкой ротации файлов.

## Установка

```bash
pip install git+https://github.com/greengoblinalex/simple-logger.git
```

## Использование

```python
from simple_logger import get_logger

# Можно передавать строку
logger = get_logger("my_app")
# или __name__ в качестве имени логгера
logger = get_logger(__name__)

logger.info("Это информационное сообщение")
logger.error("Это сообщение об ошибке")

# Логирование в файл и консоль
file_logger = get_logger("my_app", log_file="app.log")
file_logger.info("Это сообщение будет в файле и в консоли")
```

## Настройка

Вы можете настроить логгер, используя дополнительные параметры:

```python
logger = get_logger(
    name="my_app",  # Используя "root", вы настраиваете корневой логгер
    log_file="app.log",
    level="DEBUG",  # Уровень логирования
    rotation_size=5 * 1024 * 1024,  # 5 МБ для ротации
    backup_count=3  # Хранить 3 архивных файла
)
```

## Настройка через .env файл

Вы также можете настроить параметры логирования через файл `.env` в корне вашего проекта:

```
LOG_DIR=logs                # Директория для хранения логов
LOG_LEVEL=INFO              # Уровень логирования 
LOG_ROTATION_SIZE=5242880   # Размер файла для ротации (5 МБ)
LOG_BACKUP_COUNT=3          # Количество сохраняемых архивных файлов
```
