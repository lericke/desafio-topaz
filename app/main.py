

from fastapi import FastAPI
import router.endpoint as endpoint

app = FastAPI()

app.include_router(endpoint.router)