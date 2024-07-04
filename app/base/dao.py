from sqlalchemy import select, insert, delete, update
from fastapi import HTTPException, status
from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with (async_session_maker() as session):
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            res = await session.execute(query)
            return res.mappings().all()

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=model_id)
            res = await session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with (async_session_maker() as session):
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            res = await session.execute(query)
            return res.mappings().one_or_none()

    @classmethod
    async def add_one(cls, **data):
        async with (async_session_maker() as session):
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def delete(cls, model_id: int):
        async with (async_session_maker() as session):
            query = delete(cls.model).filter_by(id=model_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update(cls, model_id: int, **model_data):
        async with (async_session_maker() as session):
            check = select(cls.model.__table__.columns).filter_by(id=model_id)
            existing = await session.execute(check)
            res_existing = existing.mappings().one_or_none()
            if res_existing:
                query = update(cls.model).values(**model_data)
                await session.execute(query)
                await session.commit()
                updated = select(cls.model.__table__.columns).filter_by(id=model_id)
                res = await session.execute(updated)
                return res.mappings().one_or_none()
            else:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    @classmethod
    async def change_ordering(cls, model_id: int, ordering: list[int]):
        async with (async_session_maker() as session):
            query = update(cls.model).filter_by(id=model_id).values(ordering=ordering)
            await session.execute(query)
            await session.commit()
