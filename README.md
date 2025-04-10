# Simple Logger

Простая библиотека для логирования с цветным форматированием и поддержкой ротации файлов.

## Установка

```bash
pip install git+https://github.com/greengoblinalex/simple-logger.git
```

## Использование

```python
from simple_logger import get_logger

# Логирование только в консоль
logger = get_logger("my_app")
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
    name="my_app", 
    log_file="app.log",
    level="DEBUG",  # Уровень логирования
    rotation_size=5 * 1024 * 1024,  # 5 МБ для ротации
    backup_count=3  # Хранить 3 архивных файла
)
```
