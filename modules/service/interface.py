from abc import ABC, abstractmethod
from fastapi import APIRouter

class ServiceInterface(ABC):
    """
    Abstract interface for all services.
    Each service should implement this interface and provide its own APIRouter.
    """

    @abstractmethod
    def get_router(self) -> APIRouter:
        """
        Returns the APIRouter for the service.
        This router will be included in the main FastAPI application.
        """
        pass

    @abstractmethod
    def get_name(self) -> str:
        """
        Returns the unique name of the service.
        """
        pass

    @abstractmethod
    def get_prefix(self) -> str:
        """
        Returns the URL prefix for the service's routes.
        Example: "/users" or "/orders"
        """
        pass
