from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

class StorageInterface(ABC):
    """
    Abstract interface for persistence storage.
    Can be implemented for various backends like Memory, SQL, NoSQL, etc.
    """

    @abstractmethod
    async def save(self, key: str, value: Any) -> None:
        """Saves a value with the given key."""
        pass

    @abstractmethod
    async def get(self, key: str) -> Optional[Any]:
        """Retrieves a value by its key."""
        pass

    @abstractmethod
    async def delete(self, key: str) -> bool:
        """Deletes a value by its key. Returns True if deleted, False otherwise."""
        pass

    @abstractmethod
    async def list_all(self) -> Dict[str, Any]:
        """Returns all stored key-value pairs."""
        pass

    @abstractmethod
    async def exists(self, key: str) -> bool:
        """Checks if a key exists in storage."""
        pass
