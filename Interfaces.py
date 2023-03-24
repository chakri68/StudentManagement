from abc import abstractmethod
from PyQt6.QtWidgets import QDateTimeEdit, QLineEdit
from enum import Enum
import datetime


class TaskAppView:
  @property
  @abstractmethod
  def taskTextInput(self) -> QLineEdit:
    pass

  @property
  @abstractmethod
  def taskDeadlineInput(self) -> QDateTimeEdit:
    pass


class TaskEvent(Enum):
  TASK_ADD = 1
  TASK_CHANGE = 2


class Task:
  def __init__(self, id: int, text: str, deadline: datetime.datetime | None = None, is_completed: bool = False):
    self._id = id
    self._text = text
    self._deadline = deadline
    self._is_completed = is_completed

  def set_completed(self, value: bool):
    self._is_completed = value
    return self

  def get_text(self) -> str:
    return self._text

  def get_deadline(self) -> datetime.datetime | None:
    return self._deadline

  def get_is_completed(self) -> bool:
    return self._is_completed

  def get_id(self) -> int:
    return self._id

  def __str__(self):
    return f"Task {self._text}{f'to be completed by {self._deadline}' if self._deadline is not None else ''}"


class TaskEventListener:
  @abstractmethod
  def handle(self, event: TaskEvent, new_task: Task):
    pass


class UIEvent(Enum):
  ADD_TASK = 1
  DELETE_TASK = 2
  MARK_TASK = 3
