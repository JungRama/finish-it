from fastapi import FastAPI

app = FastAPI()


@app.get("/", description="this is get")
async def root():
    return {
        "message": "this is get"
    }

@app.post("/")
async def post():
    return {
        "message": "this is post"
    }

@app.get("/items")
async def list_items():
    return {
        "message": "list item route"
    }

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {
        "message": item_id
    }