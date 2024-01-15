from models import Note
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from typing import List


class Crud:
    async def get_all(self, session: async_sessionmaker) -> List[Note]:
        async with session() as session:
            result = await session.execute(select(Note))
            return result.scalars().all()

    async def get_by_id(self, session: async_sessionmaker, id: int) -> Note:
        async with session() as session:
            result = await session.execute(select(Note).where(Note.id == id))
            return result.scalars().first()

    async def create(self, session: async_sessionmaker, note: Note) -> None:
        async with session() as session:
            session.add(note)
            await session.commit()

    async def update(
        self, session: async_sessionmaker, note_id: int, new_note: Note
    ) -> None:
        async with session() as session:
            old_note = await session.execute(select(Note).where(Note.id == note_id))
            old_note = old_note.scalars().first()
            if old_note:
                old_note.title = new_note.title
                old_note.content = new_note.content
                await session.commit()

    async def delete(self, session: async_sessionmaker, note_id: int) -> None:
        async with session() as session:
            note = await session.execute(select(Note).where(Note.id == note_id))
            note = note.scalars().first()
            if note:
                await session.delete(note)
                await session.commit()
