import sys
from Controller import TaskAppController
from Interfaces import TaskAppView as TaskApp
from Model import TaskAppModel
from Interfaces import Task, TaskEventListener, TaskEvent
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QVBoxLayout, QLineEdit, QHBoxLayout, QPushButton


# class TaskAppViewMeta(type(QMainWindow), type(TaskEventListener), type(TaskApp)):
#   pass


class TaskAppView(QMainWindow, TaskEventListener, TaskApp):

  def __init__(self):
    super().__init__()
    self.model = TaskAppModel()
    self.model.add_listener(self)
    self.controller = TaskAppController(self.model, self)
    self.setWindowTitle('Task Manager')
    self.generalLayout = QVBoxLayout()
    centralWidget = QWidget(self)
    centralWidget.setLayout(self.generalLayout)
    self.setCentralWidget(centralWidget)
    self.setFixedWidth(300)
    self._createInputArea()
    self._createTaskGrid()

  @property
  def taskTextInput(self):
    return self._taskTextInput

  @taskTextInput.setter
  def taskTextInput(self, taskTextInput: QLineEdit):
    self._taskTextInput = taskTextInput

  def _createInputArea(self):
    inputAreaLayout = QVBoxLayout()
    self._taskTextInput = QLineEdit()
    # @todo Add the task deadline input
    # self.taskDeadLineIn = QLineEdit()
    self.addTaskButton = QPushButton(text="Add Task")
    self.addTaskButton.clicked.connect(
      self.controller.handle_add_task)
    inputAreaLayout.addWidget(self.taskTextInput)
    inputAreaLayout.addWidget(self.addTaskButton)
    self.generalLayout.addLayout(inputAreaLayout)

  def _createTaskGrid(self):
    # @note The grid layout
    self.taskListLayout = QVBoxLayout()
    self.generalLayout.addLayout(self.taskListLayout)

  def addNewTask(self, task: Task):
    newTaskLayout = QHBoxLayout()
    label = QLabel(text=task.get_text())
    deadline = QLabel(text=str(task.get_deadline()))
    isCompleted = QLabel(text=str(task.get_is_completed()))
    newTaskLayout.addWidget(label)
    newTaskLayout.addWidget(deadline)
    newTaskLayout.addWidget(isCompleted)
    self.taskListLayout.addLayout(newTaskLayout)

  def handle(self, event: TaskEvent, new_task: Task):
    match event:
      case TaskEvent.TASK_ADD:
        self.addNewTask(new_task)
      case _:
        print(f"NOTIFICATION FROM MODEL {event}")


if __name__ == "__main__":
  todoApp = QApplication([])
  todoAppWindow = TaskAppView()
  todoAppWindow.show()
  sys.exit(todoApp.exec())
