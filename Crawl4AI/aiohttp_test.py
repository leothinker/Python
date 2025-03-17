import asyncio

import aiohttp
import requests

# async def main():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(
#             "https://cuhk.edu.hk/", allow_redirects=True
#         ) as response:
#             print("Status:", response.status)
#             print("Content-type:", response.headers["content-type"])

#             html = await response.text()
#             print("Body:", html)


# asyncio.run(main())
result = requests.get("https://cuhk.edu.hk/", allow_redirects=True)
print(result.url)
print(result.text)
# if []:
#     print("good")
