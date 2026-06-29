import os
import json
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register(
    "astrbot_plugin_test_counter",
    "2671016745",
    "测试计数器插件",
    "2.0.0",  
    "https://github.com/2671016745/astrbot_plugin_test_counter"
)
class TestCounterPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        # 定义数据文件路径，使用插件专属的数据目录
        self.data_dir = os.path.join("data", "plugins", "astrbot_plugin_test_counter")
        os.makedirs(self.data_dir, exist_ok=True)
        self.data_file = os.path.join(self.data_dir, "counter.json")

        # 加载或初始化计数器
        self.counter = self._load_counter()
        logger.info(f"[TestCounter] 插件已加载，当前测试次数: {self.counter}")

    def _load_counter(self) -> int:
        """从文件加载计数"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return int(data.get("count", 0))
        except Exception as e:
            logger.error(f"[TestCounter] 读取计数文件失败: {e}")
        return 0

    def _save_counter(self):
        """保存计数到文件"""
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump({"count": self.counter}, f, ensure_ascii=False)
        except Exception as e:
            logger.error(f"[TestCounter] 保存计数文件失败: {e}")

    @filter.command("测试")
    async def test_command(self, event: AstrMessageEvent):
        """处理 /测试 命令"""
        # 原子递增并保存
        self.counter += 1
        self._save_counter()

        # ✅ 已按要求修改输出文案
        reply_msg = f"这是第{self.counter}次测试"

        # 使用 yield 发送消息，兼容 NapCat 及所有其他平台适配器
        yield event.plain_result(reply_msg)

        logger.info(f"[TestCounter] 用户 {event.get_sender_id()} 触发测试，当前次数: {self.counter}")