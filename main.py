from fastapi import FastAPI

app = FastAPI(title="Status Monitor API")

@app.get("/hello")
def read_hello():
    return "Hello World 2"