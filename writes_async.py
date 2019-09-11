import requests_async as async_requests
import requests
import datetime
import asyncio
import time
import uvloop
import sys

# uvloop.install()
r = requests.get("http://localhost:8000/total")
print("number of rows: ", r.text)

time_now = datetime.datetime.now().isoformat()


async def add_tag():
    payload = {"tag": time_now}
    await async_requests.post("http://localhost:8000/tag", json=payload)


runs = 10
rows = 1000
for i in range(runs):
    tasks = []
    for i in range(rows):
        tasks.append(add_tag())
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()
    end = time.time()
    delta = end - start
    print(f"total time: {delta}")
    write_rate = int(rows / delta)
    print(f"Rows/second: {write_rate}")
