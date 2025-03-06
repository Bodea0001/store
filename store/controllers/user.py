from uuid import UUID

from litestar import Controller, get, post, patch, delete
from litestar.di import Provide
from litestar.dto import DTOData

from domain import commands
from domain.entities.user import User
from controllers import dto
from services import user as user_service
from adapters.unitofwork import IUnitOfWork, SQLAlchemyUnitOfWork


class UserController(Controller):
    path = "/users"
    dependencies = {"uow": Provide(SQLAlchemyUnitOfWork, sync_to_thread=False)}

    @get("/{user_id:uuid}", return_dto=dto.ReturnUserDTO)
    async def get_user(self, user_id: UUID, uow: IUnitOfWork) -> User:
        user = await user_service.get_user(user_id, uow)
        return user

    @post(return_dto=dto.ReturnUserDTO)
    async def create_user(self, data: commands.CreateUser, uow: IUnitOfWork) -> User:
        user = await user_service.create_user(data, uow)
        return user

    @patch(
        "/{user_id:uuid}",
        dto=dto.UpdateUserDTO,
        return_dto=dto.ReturnUserDTO,
    )
    async def update_user(
        self,
        user_id: UUID,
        data: DTOData[commands.UpdateUser],
        uow: IUnitOfWork,
    ) -> User:
        command_data = data.create_instance(user_id=user_id)

        user = await user_service.update_user(command_data, uow)
        return user

    @delete(
        "/{user_id:uuid}",
    )
    async def delete_user(self, user_id: UUID, uow: IUnitOfWork) -> None:
        await user_service.delete_user(user_id, uow)
