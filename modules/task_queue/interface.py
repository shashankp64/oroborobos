from abc import ABC, abstractmethod
from typing import Any, Dict, Optional
from .exceptions import TaskQueueError

class TaskQueueInterface(ABC):
    """
    Abstract interface for a Task Queue.
    Allows for different backends like Memory, Redis, RabbitMQ, etc.
    """

    @abstractmethod
    async def enqueue(self, queue_name: str, task_data: Dict[str, Any]) -> str:
        """
        Enqueues a task into the specified queue.
        
        Args:
            queue_name: The name of the queue.
            task_data: The data associated with the task.
            
        Returns:
            A unique task ID.
            
        Raises:
            TaskQueueError: If there's an error enqueuing the task.
        """
        pass

    @abstractmethod
    async def dequeue(self, queue_name: str) -> Optional[Dict[str, Any]]:
        """
        Dequeues a task from the specified queue.
        
        Args:
            queue_name: The name of the queue.
            
        Returns:
            The task data, or None if the queue is empty.
            
        Raises:
            TaskQueueError: If there's an error dequeuing the task.
        """
        pass

    @abstractmethod
    async def get_queue_size(self, queue_name: str) -> int:
        """
        Returns the current size of the specified queue.
        
        Args:
            queue_name: The name of the queue.
            
        Returns:
            The number of tasks in the queue.
            
        Raises:
            TaskQueueError: If there's an error getting the size.
        """
        pass

    @abstractmethod
    async def clear_queue(self, queue_name: str) -> None:
        """
        Removes all tasks from the specified queue.
        
        Args:
            queue_name: The name of the queue.
            
        Raises:
            TaskQueueError: If there's an error clearing the queue.
        """
        pass
