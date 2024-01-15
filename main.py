from fastapi import FastAPI
from crud_operations import Crud
from database import engine
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from models import Note
from pydantic import BaseModel, ConfigDict
from datetime import datetime
from http import HTTPStatus

app = FastAPI(
    title="MyNotes API",
    version="1.0.0",
    description="MyNotes API with FastAPI using async database connectors",
    contact={
        "name": "Ayhan Oruc",
        "url": "http://www.linkedin.com/in/ayhan-oruç-601224184",
    },
)

# create session and Crud object
session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
crud = Crud()


# pydantic Note model
class NoteObject(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class NoteCreateObject(BaseModel):
    title: str
    content: str


# home route
@app.get("/")
def root():
    return {"message": "OK"}


@app.get("/notes", response_model=list[NoteObject])
async def get_all_notes():
    return await crud.get_all(session)


@app.get("/notes/{note_id}")
async def get_note_by_id(note_id: int):
    return await crud.get_by_id(session, note_id)


@app.post("/notes", status_code=HTTPStatus.CREATED)
async def create_note(note: NoteCreateObject):
    note = Note(title=note.title, content=note.content)
    await crud.create(session, note)


@app.put("/notes/{note_id}", status_code=HTTPStatus.OK)
async def update_note(note_id: int, note: NoteCreateObject):
    note = Note(title=note.title, content=note.content)
    await crud.update(session, note_id, note)


@app.delete("/notes/{note_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_note(note_id: int):
    await crud.delete(session, note_id)
