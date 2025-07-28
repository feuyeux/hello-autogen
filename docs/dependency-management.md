# 依赖管理自动化

本项目配置了多种自动依赖升级方案，确保项目依赖始终保持最新和安全。

## 配置的自动化方案

### 1. GitHub Actions 自动升级 (基础版)
- **文件**: `.github/workflows/dependency-update.yml`
- **触发**: 每周一早上8点 + 手动触发
- **功能**: 
  - 自动升级Python和Java依赖
  - 创建PR进行代码审查
  - 支持手动触发

### 2. GitHub Actions 自动升级 (高级版)
- **文件**: `.github/workflows/dependency-update-advanced.yml`
- **触发**: 每周一早上8点 + 手动触发
- **功能**:
  - 矩阵构建，并行处理Python和Java项目
  - 安全漏洞检查
  - 详细的更新报告
  - 自动运行测试
  - 支持选择更新类型 (patch/minor/major)

### 3. Dependabot 自动升级
- **文件**: `.github/dependabot.yml`
- **触发**: 每周一早上8点
- **功能**:
  - GitHub原生依赖管理
  - 支持Python pip、Java Maven、GitHub Actions
  - 自动创建PR
  - 限制同时打开的PR数量

## 使用方法

### 手动触发升级
1. 进入GitHub仓库的Actions页面
2. 选择对应的workflow
3. 点击"Run workflow"按钮

### 配置自动审查
在仓库设置中配置：
- Branch protection rules
- Required reviews
- Status checks

### 监控升级结果
- 查看Actions运行日志
- 审查自动创建的PR
- 检查测试结果

## 安全考虑

- 所有升级都会创建PR，不会直接合并到主分支
- 高级版本包含安全漏洞扫描
- 建议配置必要的代码审查流程
- 重要依赖升级建议手动验证

## 故障排除

### 常见问题
1. **权限问题**: 确保GITHUB_TOKEN有足够权限
2. **测试失败**: 检查依赖兼容性
3. **PR冲突**: 手动解决冲突后重新运行

### 禁用自动升级
如需临时禁用，可以：
- 在workflow文件中注释掉schedule触发器
- 在仓库设置中禁用对应的workflow
- 修改dependabot.yml配置