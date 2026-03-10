# MiniMax MCP Skill

调用 MiniMax Coding Plan MCP 服务。

## 环境变量（已配置）

- `MINIMAX_API_KEY`: sk-cp-K0ArP0RAoohHU2maHTBUGIRRdWs9mm2zZJL--bHccFyyDwpySZRSRWb_lLiFQPNYMKzx_zXcH4GiaN0QRdPGC6DK3rbIpF5MMaNh8hnHNxpSIe7WRHef0H0
- `MINIMAX_API_HOST`: https://api.minimaxi.com

## 使用方式

通过 exec 工具直接调用：

### 调用示例

```bash
export MINIMAX_API_KEY="sk-cp-K0ArP0RAoohHU2maHTBUGIRRdWs9mm2zZJL--bHccFyyDwpySZRSRWb_lLiFQPNYMKzx_zXcH4GiaN0QRdPGC6DK3rbIpF5MMaNh8hnHNxpSIe7WRHef0H0"
export MINIMAX_API_HOST="https://api.minimaxi.com"
uvx minimax-coding-plan-mcp -y
```

## 注意事项

- MCP 使用 JSON-RPC over stdio 通信
- 需要保持进程运行状态才能持续调用
- 建议按需启动 MCP 服务

## 需要我帮你调用时，直接说！

比如：「帮我分析这段代码 xxx」
