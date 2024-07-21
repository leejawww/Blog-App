# print("hello")
# print("world")


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "hello"}


@app.post("/")
async def hi():
    return "hi"
