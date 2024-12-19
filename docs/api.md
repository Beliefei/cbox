# CBox API 文档

本文档详细说明了 CBox 的 API 接口，包括类、方法和属性的详细说明。

## CBox 类

主要的类，负责所有仓库管理操作。

### 构造函数

```python
def __init__(self):
    """
    初始化 CBox 实例
    
    属性:
        config_file (str): 配置文件路径
        workspaces (dict): 工作空间配置
        console (Console): Rich 控制台实例
    """
```

### 工作空间管理

#### add_workspace
```python
def add_workspace(self, name: str, path: str) -> None:
    """
    添加新的工作空间
    
    参数:
        name: 工作空间名称
        path: 工作空间路径
    
    异常:
        OSError: 创建目录失败时抛出
    """
```

#### list_workspaces
```python
def list_workspaces(self) -> None:
    """
    列出所有工作空间
    
    输出:
        表格形式显示工作空间信息，包括:
        - 名称
        - 路径
        - 状态
    """
```

### 仓库操作

#### clone_repo
```python
def clone_repo(self, workspace: str, repo_url: str) -> None:
    """
    克隆远程仓库到工作空间
    
    参数:
        workspace: 工作空间名称
        repo_url: 远程仓库URL
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

#### import_local_repo
```python
def import_local_repo(self, workspace: str, repo_path: str) -> None:
    """
    导入本地仓库到工作空间
    
    参数:
        workspace: 工作空间名称
        repo_path: 本地仓库路径
    
    异常:
        git.InvalidGitRepositoryError: 无效的 Git 仓库
    """
```

#### init_repo
```python
def init_repo(self, workspace: str, repo_name: str, bare: bool = False) -> None:
    """
    在工作空间中初始化新的 Git 仓库
    
    参数:
        workspace: 工作空间名称
        repo_name: 仓库名称
        bare: 是否创建裸仓库
    
    异常:
        OSError: 创建目录失败时抛出
        git.GitCommandError: Git 操作失败时抛出
    """
```

### 状态查询

#### status
```python
def status(self, workspace: str) -> None:
    """
    显示工作空间中所有仓库的状态
    
    参数:
        workspace: 工作空间名称
    
    输出:
        表格形式显示每个仓库的:
        - 名称
        - 当前分支
        - 状态（clean/dirty）
        - 更改统计
    """
```

### Git 操作

#### pull
```python
def pull(self, workspace: str) -> None:
    """
    拉取工作空间中所有仓库的更新
    
    参数:
        workspace: 工作空间名称
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

#### push
```python
def push(self, workspace: str) -> None:
    """
    推送工作空间中所有仓库的更改
    
    参数:
        workspace: 工作空间名称
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

#### commit
```python
def commit(self, workspace: str, message: str) -> None:
    """
    提交工作空间中所有仓库的更改
    
    参数:
        workspace: 工作空间名称
        message: 提交信息
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

### 分支管理

#### list_branches
```python
def list_branches(self, workspace: str) -> None:
    """
    列出工作空间中所有仓库的分支
    
    参数:
        workspace: 工作空间名称
    
    输出:
        表格形式显示每个仓库的分支信息:
        - 分支名称
        - 是否是当前分支
        - 跟踪信息
        - 最后提交信息
    """
```

#### create_branch
```python
def create_branch(self, workspace: str, branch_name: str, start_point: str = None) -> None:
    """
    在工作空间中的所有仓库创建新分支
    
    参数:
        workspace: 工作空间名称
        branch_name: 新分支名称
        start_point: 可选，新分支的起始点
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

#### switch_branch
```python
def switch_branch(self, workspace: str, branch_name: str) -> None:
    """
    切换工作空间中所有仓库的分支
    
    参数:
        workspace: 工作空间名称
        branch_name: 目标分支名称
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

#### delete_branch
```python
def delete_branch(self, workspace: str, branch_name: str, force: bool = False) -> None:
    """
    删除工作空间中所有仓库的指定分支
    
    参数:
        workspace: 工作空间名称
        branch_name: 要删除的分支名称
        force: 是否强制删除
    
    异常:
        git.GitCommandError: Git 操作失败时抛出
    """
```

### 工具方法

#### _load_config
```python
def _load_config(self) -> dict:
    """
    加载配置文件
    
    返回:
        dict: 工作空间配置字典
    """
```

#### _save_config
```python
def _save_config(self) -> None:
    """
    保存配置到文件
    """
```

#### _get_repos_in_workspace
```python
def _get_repos_in_workspace(self, workspace: str) -> list:
    """
    获取工作空间中的所有 Git 仓库
    
    参数:
        workspace: 工作空间名称
    
    返回:
        list: Git 仓库对象列表
    """
```

## GUI 接口

### CBoxGUI 类

图形用户界面的主类，提供了可视化的仓库管理功能。

### 构造函数

```python
def __init__(self):
    """
    初始化 GUI 界面
    
    属性:
        cbox: CBox 实例
        workspaces_table: 工作空间表格
        repos_table: 仓库表格
    """
```

### 主要功能

#### 工作空间管理
- 添加新工作空间（支持文件对话框选择路径）
- 显示工作空间列表和状态
- 删除工作空间

#### 仓库操作
- 克隆新仓库
- 查看仓库状态
- 批量更新（pull）操作
- 显示分支信息和未跟踪文件

#### 用户界面组件
- 工作空间和仓库的表格视图
- 操作按钮和工具栏
- 状态提示和错误提示对话框

### 界面布局

```
主窗口
├── 工作空间标签页
│   ├── 添加工作空间区域
│   │   ├── 名称输入框
│   │   ├── 路径输入框
│   │   └── 浏览按钮
│   ├── 工作空间表格
│   └── 操作按钮组
│       ├── 克隆仓库
│       ├── 检查状态
│       └── 更新全部
└── 仓库标签页
    └── 仓库状态表格
```

## 使用示例

### 基本工作流程
```python
# 创建 CBox 实例
cbox = CBox()

# 添加工作空间
cbox.add_workspace("dev", "~/projects/dev")

# 克隆仓库
cbox.clone_repo("dev", "https://github.com/user/repo.git")

# 查看状态
cbox.status("dev")

# 创建并切换分支
cbox.create_branch("dev", "feature/new-feature")
cbox.switch_branch("dev", "feature/new-feature")

# 提交更改
cbox.commit("dev", "feat: add new feature")

# 推送更改
cbox.push("dev")
```

### 批量操作示例
```python
# 导入多个仓库
cbox.import_from_scan("dev", "~/old-projects")

# 批量更新
cbox.pull("dev")

# 批量切换分支
cbox.switch_branch("dev", "develop")
```

## 错误处理

所有方法都会适当处理异常并提供友好的错误信息。主要的异常类型包括：

1. `git.GitCommandError`: Git 操作失败
2. `git.InvalidGitRepositoryError`: 无效的 Git 仓库
3. `OSError`: 文件系统操作失败
4. `KeyError`: 工作空间不存在

建议在使用 API 时进行适当的异常处理：

```python
try:
    cbox.clone_repo("dev", "https://github.com/user/repo.git")
except git.GitCommandError as e:
    print(f"Git 操作失败: {e}")
except KeyError:
    print("工作空间不存在")
