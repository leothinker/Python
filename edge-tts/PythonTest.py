import asyncio
import os
import time

import edge_tts

# edge-tts --list-voices


async def convert(text, file_name) -> None:
    start_time = time.time()
    communicate = edge_tts.Communicate(text, "zh-CN-XiaoxiaoNeural")
    await communicate.save(f"sounds/{file_name}.mp3")
    print(f"{file_name}用时：{int(time.time() - start_time)}秒")


async def amain():
    # 创建输出文件夹
    if not os.path.exists("sounds"):
        os.makedirs("sounds")

    tasks = []
    # 遍历输入文件
    for root, dirs, files in os.walk("texts"):
        for file in files:
            # 将文件中的文本读出来
            with open(os.path.join(root, file), "r", encoding="utf-8") as text_file:
                text = text_file.read()
                # 读取文件名
                file_name, ext = os.path.splitext(file)
                # 加入任务列表
                tasks.append(convert(text, file_name))
    # 等待所有任务完成
    await asyncio.gather(*tasks)


asyncio.run(amain())
