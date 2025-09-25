from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World, azul fellawen"}


# add welcome endpoint
@app.get("/welcome")
async def welcome():
    return {"message": "Welcome to logwire!"}


# add health endpoint
@app.get("/health")
async def health():
    return {"status": "ok"}
