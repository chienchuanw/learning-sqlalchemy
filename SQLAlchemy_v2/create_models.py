from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Text
from typing import List


# Define a base class for all ORM models
class Base(DeclarativeBase):
    pass


# Define the User model class
class User(Base):
    # Define the table name in the database
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str]

    # Define a one-to-many relationship to the Comment model.
    # This means each User can have multiple Comments.
    # SQLAlchemy uses this to link User objects with their related Comment objects.
    # back_populates is used to establish a bidirectional relationship.
    # It connects this relationship with the 'user' relationship in the Comment model.
    comments: Mapped[List["Comment"]] = relationship("Comment", back_populates="user")

    # Define a string representation of the User object for debugging purposes
    def __repr__(self) -> str:
        return f"User(id={self.id}, username={self.username}, email={self.email})"


class Comment(Base):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="comments")

    def __repr__(self) -> str:
        return f"Comment(id={self.id}, user_id={self.user_id}, content={self.content})"
