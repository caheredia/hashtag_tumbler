import requests_async as async_requests
import requests
import datetime
import asyncio
import time
import uvloop

# uvloop.install()
r = requests.get("http://localhost:8000/total")
print("number of rows: ", r.text)


time_now = datetime.datetime.now().isoformat()


async def foo():
    payload = {"tag": time_now}
    await async_requests.post("http://localhost:8000/tag", json=payload)


tasks = []
rows = 100
for i in range(rows):
    tasks.append(foo())
start = time.time()
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
end = time.time()
delta = end - start
print(f"total time: {delta}")
write_rate = int(rows / delta)
print(f"Rows/second: {write_rate}")

r = requests.get("http://localhost:8000/total")
print("number of rows: ", r.text)
