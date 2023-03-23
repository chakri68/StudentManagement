from enum import Enum
from Model import TaskAppModel
from Interfaces import TaskAppView


class TaskAppController:
  def __init__(self, model: TaskAppModel, view: TaskAppView):
    self.model = model
    self.view = view

  def handle_add_task(self):
    task_text = self.view.taskTextInput.text()
    self.model.add_task(text=task_text)
