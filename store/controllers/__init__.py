from controllers.user import UserController
from controllers.auth import AuthController


controllers = [
    UserController,
    AuthController,
]

__all__ = ["controllers"]
