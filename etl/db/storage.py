from abc import ABC, abstractmethod


class Storage(ABC):
    def __call__(self):
        return self

    @abstractmethod
    async def create(self, document: dict):
        """Add new document"""
        pass

    @abstractmethod
    async def get(self, spec: dict):
        """Get a single document from the database."""
        pass
