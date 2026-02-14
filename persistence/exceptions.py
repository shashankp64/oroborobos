class StorageError(Exception):
    """Base class for all storage-related exceptions."""
    pass

class ContainerNotFoundError(StorageError):
    """Raised when the specified container is not found."""
    def __init__(self, container: str):
        self.container = container
        super().__init__(f"Container '{container}' not found.")

class KeyNotFoundError(StorageError):
    """Raised when the specified key is not found in the container."""
    def __init__(self, container: str, key: str):
        self.container = container
        self.key = key
        super().__init__(f"Key '{key}' not found in container '{container}'.")

class StorageConnectionError(StorageError):
    """Raised when there is an error connecting to the storage backend."""
    pass
