from typing import Any, Dict, Optional
from .interface import StorageInterface

class MemoryStorage(StorageInterface):
    """
    In-memory implementation of the StorageInterface.
    Note: Data will be lost when the process terminates.
    """

    def __init__(self):
        # Nested dict: self._data[container][key] = value
        self._data: Dict[str, Dict[str, Any]] = {}

    async def save(self, container: str, key: str, value: Any) -> None:
        if container not in self._data:
            self._data[container] = {}
        self._data[container][key] = value

    async def get(self, container: str, key: str) -> Optional[Any]:
        return self._data.get(container, {}).get(key)

    async def delete(self, container: str, key: str) -> bool:
        if container in self._data and key in self._data[container]:
            del self._data[container][key]
            # Clean up empty container
            if not self._data[container]:
                del self._data[container]
            return True
        return False

    async def list_all(self, container: str) -> Dict[str, Any]:
        return self._data.get(container, {}).copy()

    async def exists(self, container: str, key: str) -> bool:
        return container in self._data and key in self._data[container]
