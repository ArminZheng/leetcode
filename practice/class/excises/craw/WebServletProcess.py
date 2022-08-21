from concurrent.futures import ProcessPoolExecutor
import math
from fastapi import FastAPI
import json
# from CpuIntensive import is_prime

app = FastAPI()


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


@app.get("/is_prime/{numbers}")
def index(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = process_pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)), ensure_ascii=False)


@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    process_pool = ProcessPoolExecutor()  # 必须放在所有函数声明的最下面才能用?
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
