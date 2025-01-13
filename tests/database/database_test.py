import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, sessionmaker, declarative_base

db = sa.create_engine("sqlite:///ledger.db")
Session = sessionmaker(bind=db)
Base = declarative_base()

class Entry(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]

    def __repr__(self) -> str:
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
    
def main() -> None:
    Base.metadata.create_all(db)
    user = Entry(username="Arjan", email="Arjan@arjancodes.com")

    with Session() as session:
        session.add(user)
        session.commit()
        print(session.query(Entry).all())

if __name__ == "__main__":
    main()
