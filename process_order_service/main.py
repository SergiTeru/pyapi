"""process_order_service main module"""
from starlette.applications import Starlette
from starlette.routing import Route

from .endpoints import Homepage


app = Starlette(debug=True, routes=[
    Route('/', Homepage),
])
