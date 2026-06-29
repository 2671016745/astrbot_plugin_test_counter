# astrbot_plugin_test_counter

🔢 AstrBot 测试计数器插件 —— 发送 `/测试` 即可获取当前测试序号！

专为 AstrBot + NapCat 等适配器设计的轻量级互动插件。数据自动持久化存储，重启不丢失，开箱即用。

## ✨ 功能特性

- **一键测试**：发送 `/测试` 指令，机器人自动回复当前测试人数
- **持久化存储**：计数数据保存在本地 JSON 文件中，AstrBot 重启、插件重载均不会归零
- **全平台适配**：基于 AstrBot 标准事件接口开发，完美兼容 NapCat、LLOneBot、Chronocat 等所有适配器
- **零配置**：无需填写任何 API Key 或额外配置项，安装启用即可使用

## 📦 安装方式

### 方法一：通过 AstrBot WebUI 安装（推荐）

1. 打开 AstrBot WebUI -> 「插件市场」
2. 搜索 `astrbot_plugin_test_counter`
3. 点击「安装」并启用插件

### 方法二：手动安装

1. 将本仓库克隆或下载到 AstrBot 的插件目录：
```bash
   cd AstrBot/data/plugins/
   git clone https://github.com/your-repo/astrbot_plugin_test_counter.git
```
2. 在 AstrBot WebUI 的「插件管理」页面点击「刷新」
3. 找到 `test_counter` 插件并开启

## 🚀 使用示例

在 QQ 群或私聊中发送：/测试
机器人回复：你是第多少个测试的人
> 💡 **提示**：AstrBot 默认指令前缀为 `/`，如果你的配置修改过前缀，请以实际配置为准（例如 `#测试`）。

## 📁 数据存储

计数数据保存在以下路径：AstrBot根目录/data/plugins/astrbot_plugin_test_counter/counter.json
如需重置计数，可直接编辑该文件将 `count` 改为 `0`，或删除该文件后重新触发指令即可从 1 开始。

## 📋 插件元数据

| 字段 | 值 |
| :--- | :--- |
| 插件标识 | `astrbot_plugin_test_counter` |
| 版本 | `1.0.0` |
| 适用 AstrBot 版本 | ≥ 3.x / 4.x |
| 依赖 | 无额外第三方依赖 |

## ⚠️ 注意事项

- 当前版本为**全局计数**（所有群聊 + 私聊共享同一个计数器）
- 如需每个群独立计数，请提 Issue 或自行修改 `main.py` 中的存储逻辑
- 插件使用同步文件读写，对于普通 QQ 群场景完全足够；若并发极高（如千人群频繁触发），建议改为异步写入

## 📄 License

MIT License

## 🤝 贡献与反馈

欢迎提交 Issue 和 Pull Request！如果你觉得这个插件有用，请给一个 ⭐ Star 支持一下～