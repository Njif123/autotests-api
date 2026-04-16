import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

print(response.status_code)
print(response.json())

data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(response.status_code)
print(response.json())

data = {
    "username": "test_user",
    "password": "123123"
}
response = httpx.post("https://httpbin.org/post", data=data)
print(response.status_code)
print(response.json())

headers = {
    "Authorization": "232"
}
response = httpx.get("https://httpbin.org/get", headers=headers)

params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json())


with httpx.Client() as client:
    res1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    res2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(res1.json())
print(res2.json())


client = httpx.Client(headers={
    "Authorization": "232"
})
res = client.get("https://httpbin.org/get")
print(res.json())


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")