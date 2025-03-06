from litestar import Litestar, Router

from controllers import controllers


api_router = Router(path="/api", route_handlers=controllers)

app = Litestar(
    route_handlers=[api_router],
)
