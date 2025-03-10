import asyncio

import edge_tts

TEXT = "这个男人叫小帅，他现在正躲在屋顶，而他的女友金发妹正在找他，事情的经过还要从三个月前讲起"
VOICE = "zh-CN-YunxiNeural"
OUTPUT_FILE = "test.mp3"


async def amain() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


asyncio.run(amain())
