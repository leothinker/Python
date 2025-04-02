import asyncio

import aiohttp


async def main():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("www.diversityinc.com:443") as response:
                print("Status:", response.status)
                print("Content-type:", response.headers["content-type"])

                html = await response.text()
                print("Body:", html[:15], "...")
    except Exception as e:
        # if "response" in locals():
        print(response.status)
        # print(e.status_code)
        return False


asyncio.run(main())
