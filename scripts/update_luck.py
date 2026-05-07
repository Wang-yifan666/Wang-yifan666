import random
from datetime import datetime

README_PATH = "README.md"

levels = [
    "大吉",
    "中吉",
    "小吉",
    "末吉",
    "平",
    "小凶",
    "中凶",
    "大凶",
]

events = [
    "吃饭",
    "玩游戏",
    "看动漫",
    "考试",
    "写代码",
    "刷算法题",
    "整理博客",
    "提交 GitHub",
    "学习新知识",
    "重构旧项目",
    "读技术文档",
    "熬夜 Debug",
    "CV工程师",
    "提交代码",
    "不写注释",
    "边吃饭边改 bug",
    "打开电脑",
    "校园跑",
    "散步",
    "开会",
    "摸鱼",
]

today = datetime.now()
date_str = today.strftime("%Y-%m-%d")

level = random.choice(levels)

# 星期四疯狂加成
if today.weekday() == 3:
    events = events + ["疯狂星期四"] * 5   # 可自定义倍数

# 打乱事件顺序
shuffled = random.sample(events, len(events))

# 抽取“宜”
max_good = min(3, len(events) - 1)
good_num = random.randint(1, max_good) if max_good >= 1 else 1
good_list = shuffled[:good_num]

# 构建“忌”的候选池：从剩余事件中排除所有“疯狂星期四”（如果宜里已经有了）
remaining = shuffled[good_num:]
if "疯狂星期四" in good_list:
    remaining = [e for e in remaining if e != "疯狂星期四"]

# 抽取“忌”
max_bad = min(2, len(remaining))
bad_num = random.randint(1, max_bad) if max_bad >= 1 else 0
bad_list = random.sample(remaining, bad_num) if bad_num > 0 else []

good = "、".join(good_list)
bad = "、".join(bad_list) if bad_list else "无"

lucky_number = random.randint(1, 99)

new_content = f"""今日运势：**{level}**

宜：{good}  
忌：{bad}  
幸运数字：**{lucky_number}**

更新日期：`{date_str}`
"""

with open(README_PATH, "r", encoding="utf-8") as f:
    readme = f.read()

start = "<!-- DAILY-LUCK:START -->"
end = "<!-- DAILY-LUCK:END -->"

before = readme.split(start)[0]
after = readme.split(end)[1]

updated = before + start + "\n" + new_content + end + after

with open(README_PATH, "w", encoding="utf-8") as f:
    f.write(updated)