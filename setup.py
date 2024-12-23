from setuptools import setup, find_packages

setup(
    name="cbox-tool",
    version="0.1.14",
    packages=find_packages(),
    install_requires=[
        "click>=8.0.0",
        "pyyaml>=6.0.0",
        "rich>=13.0.0",
        "gitpython>=3.1.0",
        "PySide6>=6.6.0",
    ],
    entry_points={
        'console_scripts': [
            'cbox=cbox.cli:main',
            'cbox-gui=cbox.gui:main',
        ],
    },
    author="belief",
    author_email="beliefchinese@gmail.com",
    description="A powerful multi-repository management tool for Git projects",
    long_description="""
# CBox

A powerful multi-repository management tool with GUI support.

[English](https://github.com/Beliefei/cbox/docs/README_en.md) | [中文](https://github.com/Beliefei/cbox/docs/README_zh.md)

<div align="center">

![CBox Logo](https://github.com/Beliefei/cbox/blob/main/icon.png)

CBox is a powerful multi-repository management tool that helps you better organize and manage multiple Git repositories. It supports workspace management, batch operations, branch management, and other features, making multi-repository management simple and efficient.

CBox 是一个强大的多仓库管理工具，帮助您更好地组织和管理多个 Git 仓库。它支持工作空间管理、批量操作、分支管理等功能，让多仓库管理变得简单高效。

[![PyPI version](https://badge.fury.io/py/cbox-tool.svg)](https://badge.fury.io/py/cbox-tool)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

## Features

- **Workspace Management**
  - Create and manage multiple workspaces
  - Import existing repositories
  - Initialize new repositories
  - Scan and batch import repositories
  - Delete workspaces and all their contents

- **Repository Operations**
  - Clone remote repositories
  - Delete repositories from workspace
  - Batch execute git operations (pull, push, commit)
  - View repository status
  - Import local repositories

- **Branch Management**
  - Create, switch, and delete branches
  - Merge branches
  - View branch status
  - Batch branch operations

- **GUI Interface**
  - Cross-platform graphical interface
  - Intuitive workspace management
  - Visual repository status
  - Easy-to-use batch operations

## Installation

### Method 1: Install from PyPI (Recommended)

```bash
pip install cbox-tool
```

### Method 2: Install from Source

1. Clone the repository:
```bash
git clone https://github.com/Beliefei/cbox.git
cd cbox
```

2. Install dependencies:
```bash
pip install -e .
```

## Quick Start

### Command Line Interface

1. Create a workspace:
```bash
cbox add_workspace dev ~/projects/dev
```

2. Clone a repository to the workspace:
```bash
cbox clone dev https://github.com/user/repo.git
```

3. View workspace status:
```bash
cbox status dev
```

### Graphical Interface

1. Launch the GUI:
```bash
cbox-gui
```

2. Use the interface to:
   - Add and manage workspaces
   - Clone and manage repositories
   - Monitor repository status
   - Perform batch operations

## Basic Usage

### Workspace Management
```bash
# List all workspaces
cbox list_workspaces

# Remove a workspace
cbox remove_workspace dev
```

### Repository Operations
```bash
# Import local repository
cbox import_repo dev ~/existing-repo

# Initialize new repository
cbox init dev new-project

# Scan and import all Git repositories in a directory
cbox scan_import dev ~/old-projects

# Remove repository
cbox remove_repo dev repo-name
```

### Git Operations
```bash
# Pull updates
cbox pull dev

# Pull updates with rebase
cbox pull-rebase dev

# Commit changes
cbox commit dev "feat: add new feature"

# Push changes
cbox push dev
```

### Branch Management
```bash
# List branches
cbox branches dev

# Create new branch
cbox create_branch dev feature/new-feature

# Switch branch
cbox switch_branch dev feature/new-feature

# Delete branch
cbox delete_branch dev feature/old-feature

# Merge branch
cbox merge dev feature/new-feature
cbox merge dev feature/new-feature --no-ff # disable fast-forward merge
```

## Advanced Features

### Batch Branch Switching

Use the `switch_branch` command to switch branches in all repositories within a workspace simultaneously:

```bash
# Switch to specified branch
cbox switch_branch dev feature/new-ui
```

### Repository Scanning

Automatically import multiple Git repositories:

```bash
# Scan and import repositories
cbox scan_import dev ~/projects
```

## Best Practices

1. **Workspace Organization**
   - Group related repositories in the same workspace
   - Use descriptive workspace names
   - Keep workspace paths consistent

2. **Branch Management**
   - Check status before batch branch operations
   - Ensure no uncommitted changes
   - Use consistent branch naming conventions

3. **Batch Operations**
   - Review operation scope before execution
   - Use status command to verify results
   - Handle errors appropriately

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please:
1. Check the documentation
2. Search existing issues
3. Create a new issue if needed

For more information, visit our [GitHub repository](https://github.com/Beliefei/cbox).

---

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
git clone https://github.com/Beliefei/cbox.git
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
cbox merge dev feature/new-feature --no-ff # 禁用 fast-forward 合并
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

更多信息，请访问我们的 [GitHub 仓库](https://github.com/Beliefei/cbox)。

    """,
    long_description_content_type="text/markdown",
    url="https://github.com/Beliefei/cbox",
    project_urls={
        "Bug Tracker": "https://github.com/Beliefei/cbox/issues",
        "Documentation": "https://github.com/Beliefei/cbox/tree/main/docs",
        "Source Code": "https://github.com/Beliefei/cbox",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Version Control",
        "Topic :: Utilities",
    ],
    python_requires=">=3.8",
    keywords="git repository management tool workspace",
)
