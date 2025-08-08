import uvicorn
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api.routers import orders
from api.routers import tracking
from api.routers import index as indexRoute
from api.models import model_loader
from api.dependencies.config import conf
from api.schemas.orders import TrackingStatusSchema

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router)
app.include_router(tracking.router)

indexRoute.load_routes(app)
model_loader.index()

@app.get("/")
def read_root():
    return {"message": "API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host=conf.app_host, port=conf.app_port, reload=True)
