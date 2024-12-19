# CBox

CBox 是一个强大的多仓库管理工具，帮助您更好地组织和管理多个 Git 仓库。它支持工作空间管理、批量操作、分支管理等功能，让多仓库管理变得简单高效。

## 特性

- **工作空间管理**
  - 创建和管理多个工作空间
  - 导入现有仓库
  - 初始化新仓库
  - 扫描并批量导入仓库
  - 删除工作空间及其所有内容

- **仓库操作**
  - 克隆远程仓库
  - 删除工作空间中的仓库
  - 批量执行 git 操作（pull、push、commit）
  - 查看仓库状态
  - 导入本地仓库

- **分支管理**
  - 创建、切换、删除分支
  - 合并分支
  - 查看分支状态
  - 批量分支操作

- **图形界面**
  - 跨平台图形界面
  - 直观的工作空间管理
  - 可视化仓库状态
  - 便捷的批量操作

## 安装

### 方法 1：从 PyPI 安装（推荐）

```bash
pip install cbox-tool
```

### 方法 2：从源码安装

1. 克隆仓库：
```bash
git clone https://github.com/beliefei/cbox.git
cd cbox
```

2. 安装依赖：
```bash
pip install -e .
```

## 快速开始

### 命令行界面

1. 创建工作空间：
```bash
cbox add_workspace dev ~/projects/dev
```

2. 克隆仓库到工作空间：
```bash
cbox clone dev https://github.com/user/repo.git
```

3. 查看工作空间状态：
```bash
cbox status dev
```

### 图形界面

1. 启动图形界面：
```bash
cbox-gui
```

2. 使用界面可以：
   - 添加和管理工作空间
   - 克隆和管理仓库
   - 监控仓库状态
   - 执行批量操作

## 基本用法

### 工作空间管理
```bash
# 列出所有工作空间
cbox list_workspaces

# 删除工作空间
cbox remove_workspace dev
```

### 仓库操作
```bash
# 导入本地仓库
cbox import_repo dev ~/existing-repo

# 初始化新仓库
cbox init dev new-project

# 扫描并导入目录下的所有 Git 仓库
cbox scan_import dev ~/old-projects

# 删除仓库
cbox remove_repo dev repo-name
```

### Git 操作
```bash
# 拉取更新
cbox pull dev

# 使用 rebase 方式拉取更新
cbox pull-rebase dev

# 提交更改
cbox commit dev "feat: add new feature"

# 推送更改
cbox push dev
```

### 分支管理
```bash
# 列出分支
cbox branches dev

# 创建新分支
cbox create_branch dev feature/new-feature

# 切换分支
cbox switch_branch dev feature/new-feature

# 删除分支
cbox delete_branch dev feature/old-feature

# 合并分支
cbox merge dev feature/new-feature
```

## 高级功能

### 批量切换分支

使用 `switch_branch` 命令可以同时切换工作空间中所有仓库的分支：

```bash
# 切换到指定分支
cbox switch_branch dev feature/new-ui
```

### 仓库扫描

自动导入多个 Git 仓库：

```bash
# 扫描并导入仓库
cbox scan_import dev ~/projects
```

## 最佳实践

1. **工作空间组织**
   - 将相关仓库分组到同一工作空间
   - 使用描述性的工作空间名称
   - 保持工作空间路径一致

2. **分支管理**
   - 在执行批量分支操作前先检查状态
   - 确保没有未提交的更改
   - 使用统一的分支命名规范

3. **批量操作**
   - 执行前检查操作范围
   - 使用状态命令验证结果
   - 妥善处理错误情况

## 贡献

欢迎贡献代码！请随时提交 pull requests。

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件。

## 支持

如果遇到问题或有疑问，请：
1. 查看文档
2. 搜索已有问题
3. 必要时创建新的问题

更多信息，请访问我们的 [GitHub 仓库](https://github.com/beliefei/cbox)。
