from litestar import Litestar, Router

from controllers import controllers

from handlers.auth import jwt_auth


api_router = Router(path="/api", route_handlers=controllers)

app = Litestar(
    route_handlers=[api_router],
    on_app_init=[jwt_auth.on_app_init],
)
