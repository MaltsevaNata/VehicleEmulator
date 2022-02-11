from abc import ABC, abstractmethod


class Storage(ABC):
    def __call__(self):
        return self

    @abstractmethod
    async def get(self, spec: dict):
        """Get a single document from the database."""
        pass

    @abstractmethod
    async def get_list(self, page_size=0, page_num=0) -> dict:
        """Get paginated documents"""
        pass
