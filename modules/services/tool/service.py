from fastapi import APIRouter
from modules.service.interface import ServiceInterface
from .router import router

class ToolService(ServiceInterface):
    def get_router(self) -> APIRouter:
        return router

    def get_name(self) -> str:
        return "tool-service"

    def get_prefix(self) -> str:
        return "/tools"
