import asyncio

import edge_tts

TEXT = "这个男人叫小帅，他现在正躲在屋顶，而他的女友金发妹正在找他，事情的经过还要从三个月前讲起"
VOICE = "zh-CN-YunxiNeural"
OUTPUT_FILE = "test.mp3"


async def amain() -> None:
    """Main function"""
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)


if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    try:
        loop.run_until_complete(amain())
    finally:
        loop.close()
