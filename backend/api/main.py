from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routers import llms, mcps


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(
    lifespan=lifespan, swagger_ui_parameters={"tryItOutEnabled": True}
)
app.include_router(llms.router, prefix="/v1")
app.include_router(mcps.router, prefix="/v1")
