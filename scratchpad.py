import aiohttp
import asyncio
import uvloop


url = "http://localhost:8000/total"


async def curl(session, url, method="GET", json=None):
    async with session.request(method, url, json=json) as response:
        return await response.json()


async def main():
    async with aiohttp.ClientSession() as session:

        r = await curl(session, url, "GET")
        print(r[0])


if __name__ == "__main__":
    uvloop.install()
    asyncio.run(main())

