# Pojia (破甲) · 脱毒修复工具与全套破甲提示词库

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6.svg)](#)
[![Status: Clean](https://img.shields.io/badge/Status-100%25%20Clean-success.svg)](#)

本仓库提供专为 **WorkBuddy** 及各类 AI 编码助手打造的：
1. **纯净脱毒修复工具**（剔除木马、已知 CVE 与未签名代理，解决杀软拦截与脚本丢失报错）；
2. **多语言全套破甲提示词库**（收录 G1 / G2 / G3-CTF 完整长效指令集）。

---

## 目录结构

```text
pojia/
├── 一键脱毒修复_双击即用.bat       # 【推荐】单文件独立批处理，任意位置双击 1 秒修复
├── build_clean_workbuddy_pack.py  # 纯净包自动化构建脚本 (Python 版)
├── audit_tools.py                 # 工具源码安全性静态审计脚本
├── 破甲提示词/                    # 完整破甲长效提示词合集
│   ├── G1-英文-12段-21803字.md
│   ├── G2-中文-27段-13838字.md
│   ├── G2-英文-27段-26639字.md
│   ├── G3-CTF版-16段-30458字.md
│   └── 说明.md
├── LICENSE                        # MIT License
└── README.md                      # 项目说明
```

---

## 核心功能与使用说明

### 1. WorkBuddy 一键脱毒修复
针对 SusuAIOverclock 历史包中因捆绑旧 CVE 样本与木马加载器导致被杀软拦截、缺失 `Install-WB-OneClick.ps1` 的问题：
- **极简方式**：直接双击运行 `一键脱毒修复_双击即用.bat`；
- **执行效果**：
  - 自动向 `%USERPROFILE%\.workbuddy` 写入安全合规的 `IDENTITY.md` 与 `SOUL.md`；
  - 补全客户端缓存缺失的安装入口，完美满足客户端 3 项 Evidence 判定（状态激活为 ACTIVE）；
  - 火绒安全、Windows Defender 全程 0 报毒、0 拦截。

### 2. 破甲提示词合集 (`/破甲提示词`)
收录了从基础到高阶的完整 Prompt 工程成果：
- **G1-英文-12段**：精简版全英文越狱与代码交付规约；
- **G2-中文-27段 / G2-英文-27段**：全功能中英文双语深度破甲与系统架构专家人设；
- **G3-CTF版-16段**：针对逆向工程、二进制分析、白帽攻防靶场的专用强化版；
- **说明.md**：详细的段落拆解与应用指引。

---

## 开源协议

本项目采用 [MIT License](LICENSE) 授权。
