#!/bin/bash
# 每日AI新闻 + OpenClaw动态 定时推送
# 每天早上9点执行

LOG_FILE="/tmp/daily_ai_news.log"
echo "=== $(date) ===" >> $LOG_FILE

cd /root/.openclaw/workspace

# 用 mcporter 搜索新闻
AI_NEWS=$(mcporter call MiniMax.web_search query="AI 人工智能 新闻 2026年3月" count=10 2>&1)
OC_NEWS=$(mcporter call MiniMax.web_search query="OpenClaw AI agent 更新 2026" count=10 2>&1)

# 简单提取标题
AI_SUMMARY=$(echo "$AI_NEWS" | grep -oP '"title":\s*"\K[^"]+' | head -5 | sed 's/^/- /')
OC_SUMMARY=$(echo "$OC_NEWS" | grep -oP '"title":\s*"\K[^"]+' | head -5 | sed 's/^/- /')

REPORT="📰 **每日AI资讯播报** - $(date '+%Y年%m月%d日')

---
## 🤖 AI领域大新闻

${AI_SUMMARY:-（获取失败）}

---
## 🦞 OpenClaw 最新动态

${OC_SUMMARY:-（获取失败）}

---
💡 自动生成于每天早上9点"

# 发到飞书
openclaw message send \
  --channel feishu \
  --target "ou_de2d9ef449a48a06d00301c76aa9448d" \
  --message "$REPORT" >> $LOG_FILE 2>&1

echo "完成 $(date)" >> $LOG_FILE
