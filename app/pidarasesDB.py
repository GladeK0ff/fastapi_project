from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


engine = create_async_engine('sqlite+aiosqlite:///pidarases.db')

new_session = async_sessionmaker(engine, expire_on_commit = False)


async def get_session():
    async with new_session() as session:
        yield session


class Base(DeclarativeBase):
    pass


class PidarasModel(Base):
    __tablename__ = "pidarases_list"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    pidaras_level: Mapped[str]
    reason: Mapped[str]
    is_dota_player: Mapped[bool]
    is_cs_player: Mapped[bool]


#@app.port("/setup_db")
async def setup_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.post("/pidarases")
async def add_pidaras():
    pass


@app.get("/pidarases")
async def get_pidaras():
    pass