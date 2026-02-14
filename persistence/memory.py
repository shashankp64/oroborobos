from typing import Any, Dict, Optional
from .interface import StorageInterface

class MemoryStorage(StorageInterface):
    """
    In-memory implementation of the StorageInterface.
    Note: Data will be lost when the process terminates.
    """

    def __init__(self):
        self._data: Dict[str, Any] = {}

    async def save(self, key: str, value: Any) -> None:
        self._data[key] = value

    async def get(self, key: str) -> Optional[Any]:
        return self._data.get(key)

    async def delete(self, key: str) -> bool:
        if key in self._data:
            del self._data[key]
            return True
        return False

    async def list_all(self) -> Dict[str, Any]:
        return self._data.copy()

    async def exists(self, key: str) -> bool:
        return key in self._data
