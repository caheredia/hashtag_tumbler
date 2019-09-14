import aiohttp
import asyncio
import uvloop


total_url = "http://localhost:8000/total"
tag_url = "http://localhost:8000/tag"
save_url = "http://localhost:8000/save"


async def curl(session, url, method="GET", json=None):
    async with session.request(method, url, json=json) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:

        r = await curl(session, total_url + "/rates", "GET")
        print(r["total"])
        payload = {"method": "test", "rate": 1}
        save = await curl(session, save_url, "POST", json=payload)
        print(save)
        r = await curl(session, total_url + "/rates", "GET")
        print(r["total"])


if __name__ == "__main__":
    uvloop.install()
    asyncio.run(main())

