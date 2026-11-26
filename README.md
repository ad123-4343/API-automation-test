# 🚀 API 自动化测试框架 (API-Automation-Test)

## 📖 项目简介
本项目是一个基于 [Python/Pytest] 构建的 [RESTful API] 接口自动化测试框架。主要用于验证 [JSONPlaceholder 博客系统] 的基础增删改查（CRUD）接口功能。

## 🛠️ 技术栈
- **语言**：Python
- **测试框架**：Pytest
- **接口请求**：Requests
- **数据驱动**：PyYAML
- **CI/CD**：GitHub Actions
- **报告生成**：pytest-html

## ✨ 核心特性
1. **数据驱动测试 (DDT)**：将测试数据（URL、Method、Payload、期望结果）全部抽离到 `test_cases.yaml` 中，实现代码与数据解耦。
2. **统一接口封装**：封装底层的 `GET` 和 `POST` 请求，加入超时控制（Timeout），提升框架的健壮性。
3. **深度 JSON 断言**：不仅校验 HTTP 状态码（Status Code），还对 Response 返回的 JSON 字段进行键值对级别的深度比对。
4. **云端持续集成**：接入 GitHub Actions 流水线，每次代码 Push 后自动触发测试，并生成 HTML 可视化报告。

## 🚀 本地运行指南
1. 克隆仓库：
   ```bash
   git clone [你的GitHub仓库地址]
