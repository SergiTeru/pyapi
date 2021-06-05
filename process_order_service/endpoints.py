"""Endpoints for the process order service"""
from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse

class Homepage(HTTPEndpoint):
    async def get(self, request: Request):
        return JSONResponse({'hello': request})