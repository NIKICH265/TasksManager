from pydantic import BaseModel, ConfigDict


class Task(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    description: str


class CreateTask(Task):
    pass


class ReadTask(Task):
    id: int
    completed: bool = False


class UpdateTask(Task):
    pass


