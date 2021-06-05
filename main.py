from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request: Request):
    return JSONResponse({'hello': request})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
])