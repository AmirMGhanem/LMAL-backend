from fastapi import FastAPI
from app.api.routes import users

app=FastAPI()

app.include_router(users.router,prefix="/api/v1/users")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
