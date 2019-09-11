import requests_async as async_requests
import requests
import datetime
import asyncio
import time
import uvloop
import sqlite3


r = requests.get("http://localhost:8000/total")
print("number of rows: ", r.text)

time_now = datetime.datetime.now().isoformat()


async def add_tag():
    payload = {"tag": time_now}
    await async_requests.post("http://localhost:8000/tag", json=payload)

async def bulk_calls(tasks):
    await asyncio.gather(*tasks)

def save_rate(method, write_rate):
    """Save rates to rate table."""
    conn = sqlite3.connect("hashtag.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO rates VALUES (:method,:rate)",
        {"method": method, "rate": write_rate},
    )
    conn.commit()
    conn.close()

runs = 100
rows = 100
for i in range(runs):
    tasks = []
    for i in range(rows):
        tasks.append(add_tag())
    start = time.time()
    uvloop.install()
    asyncio.run(bulk_calls(tasks))
    end = time.time()
    delta = end - start
    print(f"total time: {delta}")
    write_rate = int(rows / delta)
    print(f"Rows/second: {write_rate}")
    save_rate(method='async_uvloop', write_rate=write_rate)
