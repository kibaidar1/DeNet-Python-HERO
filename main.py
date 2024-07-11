import uvicorn
from fastapi import FastAPI

from app.api.endpoints.polygon import polygon_router

app = FastAPI()

app.include_router(polygon_router)

if __name__ == '__main__':
    uvicorn.run(app='main:app')
