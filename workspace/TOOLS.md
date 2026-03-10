# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## 🚨 MCP Tools - 搜索/图片必用！

**记住：搜索用 mcporter！图片分析用 mcporter！永远不用 web_fetch！**

已安装 MiniMax MCP（via mcporter）：
```
mcporter call MiniMax.web_search query="xxx"   # 搜索（必用！永远第一个！）
mcporter call MiniMax.understand_image prompt="xxx" image_source="xxx"  # 图片分析（必用！）
```

## Channels

- Telegram: 5889732065
- 飞书: ou_de2d9ef449a48a06d00301c76aa9448d（已配对但接收消息有问题）

---

Add whatever helps you do your job. This is your cheat sheet.
