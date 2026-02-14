from fastapi import APIRouter, Depends
from typing import List
from .models import Runtime, RuntimeCreate, RuntimeUpdate
from modules.persistence.interface import StorageInterface
from modules.task_queue.interface import TaskQueueInterface

async def get_storage():
    pass

async def get_task_queue():
    pass

router = APIRouter()

@router.get("/", response_model=List[Runtime])
async def list_runtimes(storage: StorageInterface = Depends(get_storage)):
    """List all runtimes."""
    pass

@router.post("/", response_model=Runtime)
async def create_runtime(runtime: RuntimeCreate, 
                         storage: StorageInterface = Depends(get_storage),
                         task_queue: TaskQueueInterface = Depends(get_task_queue)):
    """Create a new runtime and possibly enqueue a startup task."""
    pass

@router.get("/{runtime_id}", response_model=Runtime)
async def get_runtime(runtime_id: str, storage: StorageInterface = Depends(get_storage)):
    """Get a runtime by ID."""
    pass

@router.put("/{runtime_id}", response_model=Runtime)
async def update_runtime(runtime_id: str, runtime: RuntimeUpdate, storage: StorageInterface = Depends(get_storage)):
    """Update a runtime configuration."""
    pass

@router.delete("/{runtime_id}")
async def delete_runtime(runtime_id: str, storage: StorageInterface = Depends(get_storage)):
    """Delete a runtime."""
    pass

@router.post("/{runtime_id}/start")
async def start_runtime(runtime_id: str, 
                        task_queue: TaskQueueInterface = Depends(get_task_queue)):
    """Start the runtime using the task queue."""
    pass

@router.post("/{runtime_id}/stop")
async def stop_runtime(runtime_id: str):
    """Stop the runtime."""
    pass
