import os

LOGLEVEL = os.getenv("LOGLEVEL", "DEBUG")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"},
    },
    "root": {
        "level": LOGLEVEL,
        "formatter": "verbose",
        "handlers": ["console"],
    },
    "handlers": {
        "console": {
            "level": LOGLEVEL,
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    }
}
