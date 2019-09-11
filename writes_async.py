import requests_async as async_requests
import requests
import datetime
import asyncio
import time
import uvloop
from writes_sql import save_rate

uvloop.install()
r = requests.get("http://localhost:8000/total")
print("number of rows: ", r.text)


async def add_tag():
    time_now = datetime.datetime.now().isoformat()
    payload = {"tag": time_now}
    await async_requests.post("http://localhost:8000/tag", json=payload)




def calculate_write_rate(rows):
    """Returns write rate to write integer number of rows."""
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
    return write_rate


def multiple_runs(rows, runs):
    """"Run writes multiple times and save results to rates table."""
    for i in range(runs):
        write_rate = calculate_write_rate(rows)
        save_rate(write_rate)


multiple_runs(rows=1000, runs=10)


r = requests.get("http://localhost:8000/total")
print("number of rows: ", r.text)
