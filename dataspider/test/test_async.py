import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(5):
            tasks.append(asyncio.ensure_future(fetch(session, f'https://httpbin.org/get?id={i}')))
        responses = await asyncio.gather(*tasks)
        print(responses)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
