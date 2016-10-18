# -*- coding: utf-8 -*-
from qa_api import login_manager
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from apiconfig import DB_URI_local
from apiconfig import DB_URI_linux
from sqlalchemy import create_engine
from flask_login import UserMixin
from database import Session

Base = declarative_base()

class MyMixin(object):
    __table_args__ = {'mysql_engine': 'InnoDB'}


class SubTask(MyMixin, Base):
    __tablename__ = 'Subtasks'
    id = Column('id',Integer,primary_key=True,)


    major_task_track_number = Column('tracknumber', String(100), ForeignKey('Tasks.tracknumber'), nullable=False)
    MajorTask = relationship("MajorTask", back_populates="subtasks")

    name = Column('subtask_name', String(50), ForeignKey('Subtask_properties.subtask_name'), nullable=False)
    property = relationship("SubtaskProperty", back_populates="subtasks")

    status = Column('current_status', Integer, nullable=False)
    benchmark = Column('benchmark', String(100), default=None)
    running_machine = Column('running_machine', String(30), default=None)
    assistant_git_dir = Column('assistant_gitDir', String(50), default=None)
    result = Column('result', String(10), default="unknown")
    # backup_path = Column('backup_path', String(100))


if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI_linux, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Base.metadata.drop_all(engine)
    # Base.metadata.remove(SubTask)
    Base.metadata.create_all(engine)






        # print Todo.__table__
        # Base.metadata.create_all(engine)

        # print User.__table__




        # session.add(ed_user)
        # session.commit()


        # u = session.query(User).filter_by(id=3).first()
        # session.delete(u)
        # session.commit()

        # second_user = User(name='second', fullname='second second', password='secondspassword')
        # session.add(second_user)
        # session.commit()
