import json


def toJson(data):
    return json.dumps(data)


def fromJson(data: str):
    return json.loads(data)


if __name__ == "__main__":
    data = [{"name": "zhangsan中", "age": 18}, {"name": "lisi", "age": 19}]
    print(type(data))

    # dumps 将对象转换为json
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    print(type(data))

    # loads 将json转换为对象
    data = json.loads(data)
    print(data)
    print(type(data))
