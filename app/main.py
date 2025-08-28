from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# add welcome endpoint
@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to logwire!"}
