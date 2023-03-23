import datetime
from typing import List
from Interfaces import Task, TaskEventListener, TaskEvent


class TaskAppModel():
  def __init__(self, tasks: List[Task] = []):
    self.tasks = tasks
    self.new_task_listeners: List[TaskEventListener] = []
    self.task_change_listeners: List[TaskEventListener] = []

  def add_task(self, text: str, deadline: datetime.datetime | None = None, is_completed: bool = False):
    new_task = Task(len(self.tasks), text, deadline, is_completed)
    self.tasks.append(new_task)
    for listener in self.new_task_listeners:
      listener.handle(TaskEvent.TASK_ADD, new_task)

  def change_task(self, task_id: int, is_completed: bool):
    self.tasks[task_id].set_completed(is_completed)
    for listener in self.task_change_listeners:
      listener.handle(TaskEvent.TASK_CHANGE, self.tasks[task_id])

  def add_listener(self, listener: TaskEventListener):
    # @todo Add individual event listeners
    self.new_task_listeners.append(listener)
    self.task_change_listeners.append(listener)
