from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from .exceptions import StorageError, ContainerNotFoundError, KeyNotFoundError

class StorageInterface(ABC):
    """
    Abstract interface for persistence storage.
    Can be implemented for various backends like Memory, SQL, NoSQL, etc.
    """

    @abstractmethod
    async def save(self, container: str, key: str, value: Any) -> None:
        """
        Saves a value with the given key in a specific container.

        Raises:
            StorageError: If there's an error during the save operation.
        """
        pass

    @abstractmethod
    async def get(self, container: str, key: str) -> Optional[Any]:
        """
        Retrieves a value by its key from a specific container.

        Returns None if the key or container is not found.

        Raises:
            StorageError: If there's an error during the retrieval.
        """
        pass

    @abstractmethod
    async def delete(self, container: str, key: str) -> bool:
        """
        Deletes a value by its key from a specific container. 
        Returns True if deleted, False otherwise.

        Raises:
            StorageError: If there's an error during the deletion.
        """
        pass

    @abstractmethod
    async def list_all(self, container: str) -> Dict[str, Any]:
        """
        Returns all stored key-value pairs in a specific container.

        Raises:
            ContainerNotFoundError: If the specified container does not exist.
            StorageError: If there's an error listing the contents.
        """
        pass

    @abstractmethod
    async def exists(self, container: str, key: str) -> bool:
        """
        Checks if a key exists in a specific container.

        Raises:
            StorageError: If there's an error checking for existence.
        """
        pass
