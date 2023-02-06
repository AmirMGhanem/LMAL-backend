from fastapi import FastAPI
from app.api.routes import user,customer

app=FastAPI()

app.include_router(user.router,prefix="/api/v1/user")
app.include_router(customer.router,prefix="/api/v1/customer")



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
