from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import Tasks
from schemas import CreateTask, UpdateTask


def register_task(
        task: CreateTask,
        session: Session,
):
    tasks = task.model_dump()
    new_task = Tasks(**tasks)
    session.add(new_task)
    session.commit()
    return new_task


def get_task(
        idx: int,
        session: Session,
):
    stmt = select(Tasks).where(Tasks.id == idx)
    task = session.scalar(stmt)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    return task


def get_all_tasks(
    session: Session
):
    stmt = select(Tasks)
    tasks = session.scalars(stmt).all()
    return tasks


def update_task(
        idx: int,
        data: UpdateTask,
        session: Session,
):
    task = get_task(idx, session)
    task.title = data.title
    task.description = data.description
    session.commit()
    return task


def execute_task(
        idx: int,
        session: Session,
):
    task = get_task(idx, session)
    if not task.completed:
        task.completed = True
        session.commit()
        return task
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="the task has already been completed")


def delete_task(
        idx: int,
        session: Session,
):
    stmt = get_task(idx, session)
    session.delete(stmt)
    session.commit()
    return f'task {stmt.title} was deleted'
