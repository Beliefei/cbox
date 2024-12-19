# CBox 开发文档

本文档面向希望参与 CBox 开发的开发者，详细说明了项目结构、开发流程和关键概念。

## 项目结构

```
cbox/
├── cbox/               # 主要源代码目录
│   ├── __init__.py    # 包初始化文件
│   ├── mybox.py       # 核心功能实现
│   ├── cli.py         # 命令行接口实现
│   └── gui.py         # 图形界面实现
├── docs/              # 文档目录
│   ├── api.md         # API 文档
│   └── development.md # 开发文档
├── tests/             # 测试目录
├── requirements.txt   # 依赖配置
├── setup.py          # 包配置文件
└── README.md         # 项目说明
```

## 开发环境设置

1. **克隆仓库**
```bash
git clone https://github.com/beliefei/cbox.git
cd cbox
```

2. **创建虚拟环境**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **安装依赖**
```bash
pip install -e ".[dev]"
```

## 核心概念

### 1. 工作空间 (Workspace)
- 工作空间是仓库的逻辑分组
- 每个工作空间对应一个物理目录
- 工作空间配置存储在 `~/.mybox.yaml`

### 2. 仓库管理
- 支持克隆、导入和初始化仓库
- 使用 GitPython 进行 Git 操作
- 批量操作时保证原子性

### 3. 用户界面
#### 命令行界面 (CLI)
- 使用 Click 框架构建
- 支持命令分组和嵌套
- 统一的错误处理机制

#### 图形界面 (GUI)
- 使用 PySide6 (Qt) 构建
- 支持跨平台运行
- 提供直观的可视化操作

## 开发指南

### 1. 添加新功能

1. 在 `CBox` 类中添加方法：
```python
def new_feature(self, workspace, ...):
    """实现新功能的方法"""
    pass
```

2. 在 CLI 部分添加命令：
```python
@cli.command()
@click.argument('workspace')
def new_feature(workspace):
    """新命令的帮助文档"""
    CBox().new_feature(workspace)
```

3. 在 GUI 部分添加功能：
```python
def add_new_feature(self):
    """添加新功能到 GUI"""
    try:
        self.cbox.new_feature(workspace)
        QMessageBox.information(self, "成功", "操作完成")
    except Exception as e:
        QMessageBox.warning(self, "错误", str(e))
```

### 2. 错误处理

使用统一的错误处理模式：
```python
try:
    # 操作代码
    self.console.print("[green]Success message")
except Exception as e:
    self.console.print(f"[red]Error: {str(e)}")
```

### 3. 输出格式化

#### CLI 输出
使用 Rich 库进行输出格式化：
```python
table = Table(show_header=True)
table.add_column("Column1")
table.add_column("Column2")
self.console.print(table)
```

#### GUI 输出
使用 Qt 的表格和消息框：
```python
self.table.setItem(row, col, QTableWidgetItem(text))
QMessageBox.information(self, "标题", "消息")
```

## 测试指南

### 1. 单元测试
```python
def test_workspace_creation():
    cbox = CBox()
    cbox.add_workspace("test", "/tmp/test")
    assert "test" in cbox.workspaces
```

### 2. GUI 测试
```python
def test_gui_workspace_add():
    app = QApplication([])
    window = CBoxGUI()
    window.workspace_name_input.setText("test")
    window.workspace_path_input.setText("/tmp/test")
    window.add_workspace()
    assert "test" in window.cbox.workspaces
```

## 代码风格

1. **Python 风格指南**
   - 遵循 PEP 8
   - 使用 4 空格缩进
   - 最大行长度 88 字符

2. **文档字符串**
   - 使用 Google 风格的文档字符串
   - 包含参数和返回值说明
   - 提供使用示例

3. **GUI 开发规范**
   - 使用描述性的变量名
   - 保持界面简洁清晰
   - 实现响应式布局

## 发布流程

1. **版本号管理**
   - 遵循语义化版本规范
   - 在 `__init__.py` 中更新版本号
   - 创建版本标签

2. **发布检查清单**
   - 运行测试套件
   - 更新文档
   - 更新 CHANGELOG.md
   - 创建发布分支

3. **发布步骤**
   ```bash
   # 更新版本号
   edit cbox/__init__.py
   
   # 创建发布提交
   git commit -am "Release v1.0.0"
   
   # 创建标签
   git tag v1.0.0
   
   # 推送到远程
   git push origin master --tags
   ```

## 故障排除

### 1. 常见问题

1. **导入失败**
   - 检查 Python 路径
   - 验证依赖安装
   - 检查文件权限

2. **GUI 问题**
   - 确认 Qt 依赖安装正确
   - 检查系统兼容性
   - 验证显示设置

### 2. 调试技巧

1. **使用日志**
```python
import logging
logging.debug("Debug message")
```

2. **GUI 调试**
```python
# 添加调试信息
print(f"Current workspace: {self.current_workspace}")
# 使用 Qt 的调试工具
from PySide6.QtCore import qDebug
qDebug("Debug message")
```

## 性能优化

1. **批量操作优化**
   - 使用并行处理
   - 实现增量更新
   - 优化文件系统操作

2. **GUI 性能**
   - 使用延迟加载
   - 优化刷新机制
   - 减少不必要的重绘
