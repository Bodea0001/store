from uuid import UUID
from dataclasses import dataclass


class Command:
    pass


@dataclass
class CreateUser(Command):
    first_name: str
    last_name: str
    patronymic: str
    email: str
    password: str


@dataclass()
class UpdateUser(Command):
    user_id: UUID
    first_name: str | None = None
    last_name: str | None = None
    patronymic: str | None = None
    email: str | None = None
    password: str | None = None
