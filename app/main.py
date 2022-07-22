import uvicorn
from fastapi import FastAPI
from routes.api import router as api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
    print("running")
