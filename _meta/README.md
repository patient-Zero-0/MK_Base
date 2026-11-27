# _meta · 索引与统计

本目录存放自动/半自动维护的元数据文件，**不属于知识条目本身**。

| 文件 | 说明 | 维护方式 |
|---|---|---|
| `index.md` | 全库条目索引（按章节分组） | 自动（`scripts/build_index.py`） |
| `todo.md` | 悬空引用待办清单 + 远期"未来悬空"记录 | 自动（`check_dangling_refs.py --report`）+ 手工 |
| `dangling.md` | 最近一次悬空引用扫描报告 | 自动（CI 生成） |
| `analytics.json` | Cloudflare Web Analytics 每日 PV 同步结果 | 自动（cron job，待接入） |
| `dependency-graph.json` | 条目依赖图，用于前端「关系视图」 | 半自动（`scripts/build_dependency_graph.py`） |
| `m2-plan.md` | M2 数学分析 Ch3–Ch5 规划与批次拆解 | 手工（M2 启动时写定，按节奏微调） |
| `deployment-checklist.md` | 部署接入运维参考（GitHub + Cloudflare） | 手工（M0 落地后存档） |

> 自动维护文件请勿手工编辑（除非工具尚未实现该字段）。
> 手工维护文件随相应里程碑节奏更新。
