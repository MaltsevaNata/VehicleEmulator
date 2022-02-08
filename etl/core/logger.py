LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "loggers": {
        "etl": {
            "handlers": ["console"],
            "level": "INFO",
        }
    },
    "root": {
        "level": "INFO",
        "formatter": "verbose",
        "handlers": ["console"],
    },
}
