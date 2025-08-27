from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# an additional comment
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}


# add welcome endpoint
@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to logwire!"}
