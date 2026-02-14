class TaskQueueError(Exception):
    """Base class for task queue exceptions."""
    pass

class TaskEnqueueError(TaskQueueError):
    """Raised when a task cannot be enqueued."""
    pass

class TaskDequeueError(TaskQueueError):
    """Raised when a task cannot be dequeued."""
    pass
