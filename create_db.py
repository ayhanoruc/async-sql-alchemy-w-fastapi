from database import Base, engine
import asyncio


async def create_db():
    async with engine.begin() as conn:
        from models import (
            Note,
        )  # necessary to introduce Base here, to which Note inherits/binds/registered.

        await conn.run_sync(
            Base.metadata.drop_all
        )  # reset the database for fresh start
        await conn.run_sync(
            Base.metadata.create_all
        )  # create all the tables registered in Base.

    await engine.dispose()  # close connection


# lets create the database
asyncio.run(create_db())
