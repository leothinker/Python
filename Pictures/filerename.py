import os
from glob import glob


def batch_rename(folder, prefix="", width=3):
    # 收集指定后缀 jpg 文件，并按文件名排序
    paths = sorted(glob(os.path.join(folder, "*.jpg")))
    for idx, old_path in enumerate(paths, start=1):
        ext = os.path.splitext(old_path)[1]
        new_name = f"{prefix}{str(idx).zfill(width)}{ext}"
        new_path = os.path.join(folder, new_name)
        print(f"Renaming:\n  {old_path}\n  → {new_path}")
        os.rename(old_path, new_path)


if __name__ == "__main__":
    batch_rename("example", prefix="", width=4)
