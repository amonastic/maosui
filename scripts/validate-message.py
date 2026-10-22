#!/usr/bin/env python3
"""第二条消息硬校验。不通过则退出码 1，调用方不得输出该消息。

用法：
    python3 scripts/validate-message.py message.txt --greeting greeting.txt

message.txt 为纯文本正文；greeting.txt 可选，用于检查是否重复了招呼语。
"""

import argparse
import re
import sys

URL = re.compile(r"(https?://|www\.|\b[\w-]+\.(?:com|cn|net|org|io|dev|me|ai|app)\b)", re.I)
PHONE = re.compile(r"(?<!\d)1[3-9]\d{9}(?!\d)")
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")
IM = re.compile(r"(微信|威信|weixin|wechat|vx|v信|扣扣|qq)\s*[:：]?\s*[A-Za-z0-9_-]{3,}", re.I)

MIN_CHARS = 80
MAX_CHARS = 150


def main() -> int:
    ap = argparse.ArgumentParser(description="毛遂第二条消息硬校验")
    ap.add_argument("message", help="消息正文文件（UTF-8）")
    ap.add_argument("--greeting", help="招呼语文件（可选），用于检查是否重复")
    args = ap.parse_args()

    with open(args.message, encoding="utf-8") as f:
        text = f.read().strip()

    problems = []
    if URL.search(text):
        problems.append("含链接或域名")
    if PHONE.search(text):
        problems.append("含手机号")
    if EMAIL.search(text):
        problems.append("含邮箱")
    if IM.search(text):
        problems.append("含微信/QQ 等 IM 账号")

    length = len(re.sub(r"\s", "", text))
    if not MIN_CHARS <= length <= MAX_CHARS:
        problems.append(f"字数 {length}，要求 {MIN_CHARS}–{MAX_CHARS}（不计空白）")

    if args.greeting:
        with open(args.greeting, encoding="utf-8") as f:
            greeting = f.read().strip()
        if greeting and greeting in text:
            problems.append("重复了招呼语原文")

    if problems:
        for p in problems:
            print(f"FAIL: {p}")
        print("这条消息不能发出，重写。")
        return 1

    print(f"OK: {length} 字，无链接 / 无手机号 / 无邮箱 / 无 IM 账号 / 未重复招呼语")
    return 0


if __name__ == "__main__":
    sys.exit(main())
