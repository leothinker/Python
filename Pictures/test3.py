import random
from datetime import datetime, timedelta


def random_times(start_time: str, end_time: str, count: int):
    """
    从 start_time 到 end_time 范围内随机生成 count 个不重复时间点。

    :param start_time: 开始时间，格式 "HH:MM"
    :param end_time: 结束时间，格式 "HH:MM"
    :param count: 需要的时间点数量
    :return: 排序后时间点列表，格式为 "HH:MM:SS"
    """
    fmt = "%H:%M"
    start_dt = datetime.strptime(start_time, fmt)
    end_dt = datetime.strptime(end_time, fmt)

    start_sec = start_dt.hour * 3600 + start_dt.minute * 60
    end_sec = end_dt.hour * 3600 + end_dt.minute * 60

    # 在 [start_sec, end_sec] 范围内随机生成 count 个不重复秒数
    random_secs = random.sample(range(start_sec, end_sec + 1), count)

    # 转换为时间字符串并排序
    results = []
    for sec in random_secs:
        h = sec // 3600
        m = (sec % 3600) // 60
        s = sec % 60
        results.append(f"{h:02d}:{m:02d}:{s:02d}")
    return results


if __name__ == "__main__":
    # times = random_times("8:35", "8:50", 5)
    # times = random_times("13:00", "13:00", 5)
    times = random_times("17:45", "18:30", 5)
    for t in times:
        print(t)
