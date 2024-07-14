from app.base.dao import BaseDAO
from app.spaces.models import Spaces
from app.database import async_session_maker
from sqlalchemy import update, select

from app.exceptions import AlreadyInAllowed, NotInAllowed


class SpacesDAO(BaseDAO):
    model = Spaces

    @classmethod
    async def get_allowed_users(cls, space_id):
        async with (async_session_maker() as session):
            select_query = select(cls.model.__table__.columns).filter_by(id=space_id)
            res = await session.execute(select_query)
            return res.mappings().first().allowed_users

    @classmethod
    async def add_allowed_user(cls, space_id, user_id):
        async with (async_session_maker() as session):
            allowed_users = await cls.get_allowed_users(space_id)
            if user_id not in allowed_users:
                allowed_users.append(user_id)
            else:
                raise AlreadyInAllowed
            query = update(cls.model).filter_by(id=space_id).values(allowed_users=allowed_users)
            await session.execute(query)
            await session.commit()
            return allowed_users

    @classmethod
    async def delete_allowed_user(cls, space_id, user_id):
        async with (async_session_maker() as session):
            allowed_users = await cls.get_allowed_users(space_id)
            if user_id in allowed_users:
                allowed_users.remove(user_id)
            else:
                raise NotInAllowed
            query = update(cls.model).filter_by(id=space_id).values(allowed_users=allowed_users)
            await session.execute(query)
            await session.commit()
            return allowed_users
