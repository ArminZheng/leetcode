from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI
import json
import time


app = FastAPI()
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return "file result"


def read_api():
    time.sleep(0.2)
    return "api result"


def read_db():
    time.sleep(0.3)
    return "db result"


@app.get("/index")
def index():
    result_file = pool.submit(read_file)
    result_api = pool.submit(read_api)
    result_db = pool.submit(read_db)
    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result()
    })


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
