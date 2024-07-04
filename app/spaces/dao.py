from app.base.dao import BaseDAO
from app.spaces.models import Spaces
from app.database import async_session_maker
from sqlalchemy import update


class SpacesDAO(BaseDAO):
    model = Spaces

    @classmethod
    async def edit_allowed_users(cls, space_id, allowed_users):
        async with (async_session_maker() as session):
            query = update(cls.model).filter_by(id=space_id).values(allowed_users=allowed_users)
            await session.execute(query)
            await session.commit()
