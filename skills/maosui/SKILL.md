---
name: maosui
description: 把「在招聘平台上开口」变成一项技能。读简历建档、按 JD 匹配打分、为值得开口的岗位生成平台自动招呼语之后的第二条消息。当用户提供简历、岗位 JD，或要求评估岗位匹配度、撰写求职开场白时使用。
---

# 毛遂

把求职里「开口」这一步做成可执行的流程。产物是**第二条消息**——平台自动发出的固定招呼语之后，针对具体 JD 定制的那一条。

## 先读什么

| 场景 | 读这个 |
|---|---|
| 第一次使用 / 提供简历 | `workflow/00-profile.md` |
| 有一批 JD，判断值不值得开口 | `workflow/01-screen.md` |
| 已圈选岗位，要写消息 | `workflow/02-open.md` |
| 需要平台的会话机制与约束 | `platforms/platform-a.md` |
| 要生成档案文件 | `templates/profile.md` |

## 两条不可协商的规则

1. **筛选与写文案必须分两步。** 判断值和文案不能在同一轮输出。文案先出现会推着用户发送，筛选就失效了。
2. **不伪造。** 不新增简历里没有的经历，不改数字，不调时间线。

## 产物落在哪

档案写入 `.maosui/profile.md`，已由 `.gitignore` 排除，不会入库。

## 硬校验（仅能执行代码的环境）

```bash
python3 scripts/validate-message.py msg.txt --greeting greeting.txt
```

退出码非 0 时不得输出该消息。不能执行代码的环境下退化为自检行，见 `workflow/02-open.md`。
