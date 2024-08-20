from sqlalchemy import select, update

from app.base.dao import BaseDAO
from app.database import async_session_maker
from app.exceptions import NoVerificationTokenForYourEmail, UserAbsent
from app.users.models import Users


class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def change_to_verified(cls, email: str):
        async with (async_session_maker() as session):
            check = select(Users.__table__.columns).filter_by(email=email)
            existing = await session.execute(check)
            res_existing = existing.mappings().one_or_none()
            if res_existing:
                query = update(Users).values(is_verified=True).filter_by(email=email)
                await session.execute(query)
                await session.commit()
                updated = select(Users.__table__.columns).filter_by(email=email)
                res = await session.execute(updated)
                return res.mappings().one_or_none()
            else:
                raise NoVerificationTokenForYourEmail


    @classmethod
    async def reset_password(cls, email: str, new_hashed_password: str):
        async with (async_session_maker() as session):
            check = select(Users.__table__.columns).filter_by(email=email)
            existing = await session.execute(check)
            res_existing = existing.mappings().one_or_none()
            if res_existing:
                query = update(Users).values(hashed_password=new_hashed_password).filter_by(email=email)
                await session.execute(query)
                await session.commit()
                updated = select(Users.__table__.columns).filter_by(email=email)
                res = await session.execute(updated)
                return res.mappings().one_or_none()
            else:
                raise UserAbsent