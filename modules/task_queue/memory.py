import asyncio
import uuid
from collections import deque
from typing import Any, Dict, Optional, List
from .interface import TaskQueueInterface

class MemoryTaskQueue(TaskQueueInterface):
    """
    In-memory implementation of TaskQueueInterface.
    Note: Tasks are lost when the process terminates.
    """

    def __init__(self):
        # Dict mapping queue names to deques of tasks
        self._queues: Dict[str, deque] = {}

    async def enqueue(self, queue_name: str, task_data: Dict[str, Any]) -> str:
        if queue_name not in self._queues:
            self._queues[queue_name] = deque()
        
        task_id = str(uuid.uuid4())
        # Wrap task data with metadata
        wrapped_task = {
            "task_id": task_id,
            "data": task_data
        }
        self._queues[queue_name].append(wrapped_task)
        return task_id

    async def dequeue(self, queue_name: str) -> Optional[Dict[str, Any]]:
        if queue_name not in self._queues or not self._queues[queue_name]:
            return None
        
        return self._queues[queue_name].popleft()

    async def get_queue_size(self, queue_name: str) -> int:
        if queue_name not in self._queues:
            return 0
        return len(self._queues[queue_name])

    async def clear_queue(self, queue_name: str) -> None:
        if queue_name in self._queues:
            self._queues[queue_name].clear()
