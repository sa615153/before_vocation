from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from apiconfig import DB_URI_linux

Session = sessionmaker(autocommit=False,
                       autoflush=False,
                       bind=create_engine(DB_URI_linux,echo=False))


