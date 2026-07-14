from fastapi import FastAPI
import Users

app = FastAPI()

app.include_router(Users.router)

@app.get("/")
def front_door():
    return {"message": "Welcome to the Main Mall!"}