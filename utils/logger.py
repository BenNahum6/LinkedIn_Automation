import logging

# Creating a Central Logger
logger = logging.getLogger("automation_logger")
logger.setLevel(logging.INFO)

# Detailed format for logs in the file
file_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Simpler format for console logs
console_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# FileHandler – for writing to a file
file_handler = logging.FileHandler("test_logs.log", mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)

# StreamHandler – for printing to the console
console_handler = logging.StreamHandler()
console_handler.setFormatter(console_formatter)

# Adding Handlers to the Logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Makes sure Pytest recognizes the logger
logging.getLogger().setLevel(logging.INFO)
