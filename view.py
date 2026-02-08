from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import crud, schemas
from database import db_helper

router = APIRouter(tags=["tasks"])


@router.post("/tasks")
def create_task(
        task: schemas.CreateTask,
        session: Session = Depends(db_helper.session_depends),
):
    new_task = crud.register_task(task, session)
    return schemas.ReadTask.model_validate(new_task)


@router.get("/tasks")
def get_all_tasks(
        session: Session = Depends(db_helper.session_depends),
):
    tasks = crud.get_all_tasks(session)
    return tasks


@router.get("/tasks/{idx}")
def get_one_task(
        idx: int,
        session: Session = Depends(db_helper.session_depends),
):
    task = crud.get_task(idx, session)
    return schemas.ReadTask.model_validate(task)


@router.patch("/tasks/{idx}")
def execute_task(
        idx: int,
        session: Session = Depends(db_helper.session_depends),
):
    task = crud.execute_task(idx, session)
    return schemas.ReadTask.model_validate(task)


@router.put("/tasks/{idx}")
def update_task(
        idx: int,
        data: schemas.UpdateTask,
        session: Session = Depends(db_helper.session_depends),
):
    new_task = crud.update_task(idx, data, session)
    return schemas.ReadTask.model_validate(new_task)


@router.delete("/tasks/{idx}")
def delete_task(
        idx: int,
        session: Session = Depends(db_helper.session_depends),
):
    task = crud.delete_task(idx, session)
    return task
