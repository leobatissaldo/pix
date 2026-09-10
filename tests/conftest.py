import pytest
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import sessionmaker, Session
from database import Base

TEST_DATABASE_URL = "postgresql+psycopg://postgres:leo@localhost:5432/mock_pix_test"

engine = create_engine(TEST_DATABASE_URL)
TestSessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def get_test_db():
    Base.metadata.create_all(bind=engine)
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)