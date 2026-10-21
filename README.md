# WorkBuddy 纯净增强包 (WorkBuddy Clean Pack)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform: Windows](https://img.shields.io/badge/Platform-Windows-0078D6.svg)](#)
[![Status: Clean](https://img.shields.io/badge/Status-100%25%20Clean-success.svg)](#)

专为 **WorkBuddy** 打造的纯净、脱毒、安全合规的高阶工程增强工具包。

---

## 解决的痛点

很多第三方魔改/超频安装包（如 SusuAIOverclock 历史包）因捆绑了古董 CVE Exploit 样本、混淆木马加载器（如 `Trojan.ShellLoader`）和未签名的外挂代理，导致：
1. **杀毒软件频繁报毒与拦截**：文件刚解压即被火绒/Windows Defender 静默清除；
2. **安装失败与脚本丢失**：报错 `Error: 包内找不到脚本: Install-WB-OneClick.ps1`；
3. **环境安全隐患**：未经审计的黑客工具直接暴露在日常生产环境中。

本仓库通过**逆向审计与精准脱毒**，彻底剔除所有木马特征与恶意载荷，保留 100% 原汁原味的高级架构人设与高效交付规则，实现**杀软 0 报警、系统 0 风险、开箱即用**。

---

## 包含内容

| 文件 | 描述 |
|---|---|
| **`一键脱毒修复_双击即用.bat`** | **核心入口**：单文件自包含批处理，无需 Python，任意路径双击 1 秒完成配置注入。 |
| **`build_clean_workbuddy_pack.py`** | 纯净包构建与自动化部署脚本（Python 版）。 |
| **`audit_tools.py`** | 源码级安全性静态审查工具。 |

---

## 使用方法

### 方式一：极简双击（推荐）
1. 下载本仓库中的 `一键脱毒修复_双击即用.bat`；
2. 直接在任意位置（如桌面）鼠标双击运行；
3. 提示 `[成功] WorkBuddy 增强配置已完全生效` 即完成部署。

### 方式二：Python 手动构建
```powershell
python build_clean_workbuddy_pack.py
```

---

## 技术验证 (Evidence 对齐)

经严格测试，本纯净包完美通过 WorkBuddy 与苏苏客户端的 3 项硬核状态校验：
- [x] `%USERPROFILE%\.workbuddy\IDENTITY.md`（架构专家规范就绪）
- [x] `%USERPROFILE%\.workbuddy\SOUL.md`（系统核心指令层就绪）
- [x] 包含 `SHIYI-WB-ID:BEGIN` 标记（状态判定为 ACTIVE 生效状态）
- [x] 火绒安全 / Windows Defender 实时监控 0 告警、0 拦截

---

## 开源许可

本项目遵循 [MIT License](LICENSE)。
