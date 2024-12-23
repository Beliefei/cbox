"""Internationalization support for CBox GUI."""

# 语言配置
TRANSLATIONS = {
    "en": {
        "workspace": "Workspace",
        "add": "Add",
        "remove": "Remove",
        "clone": "Clone",
        "import": "Import",
        "batch_import": "Batch Import",
        "branch_action": "Branch Action",
        "create_branch": "Create Branch",
        "switch_branch": "Switch Branch",
        "merge_branch": "Merge Branch",
        "commit": "Commit",
        "push": "Push",
        "pull": "Pull",
        "refresh": "Refresh",
        "status": "Status",
        "settings": "Settings",
        "language": "Language",
        "repo_name": "Repository",
        "current_branch": "Branch",
        "untracked": "Untracked",
        "last_commit": "Last Commit",
        "error": "Error",
        "success": "Success",
        "info": "Information",
        "select_workspace": "Please select a workspace",
        "select_repo": "Please select a repository",
        "confirm_delete": "Confirm Delete",
        "confirm_remove": "Confirm Remove",
        "enter_commit_msg": "Enter commit message...",
        "changes_committed": "Changes committed successfully",
        "changes_pushed": "Changes pushed successfully",
        "commit_msg_required": "Please enter a commit message",
        "branch_name": "Branch name",
        "start_point": "Start point (optional)",
        "select_branch": "Select branch",
        "branch_created": "Branch created successfully",
        "branch_switched": "Branch switched successfully",
        "branch_merged": "Branch merged successfully",
        "confirm": "Confirm",
        "cancel": "Cancel",
        "browse": "Browse",
        "path": "Path",
        "cbox_manager": "CBox Manager",
        "workspace_name": "Workspace Name",
        "workspace_path": "Workspace Path",
        "input_workspace_name": "Enter workspace name",
        "select_workspace_path": "Select workspace path",
        "select_workspace_directory": "Select Workspace Directory",
        "input_branch_name": "Enter branch name",
        "optional_start_point": "Optional, leave empty to create from current branch",
        "input_commit_message": "Enter commit message",
        "has_changes": "Has Changes",
        "clean": "Clean",
        "no_commits": "No commits",
        "no_changes_to_commit": "No changes to commit",
        "no_changes_to_push": "No changes to push",
        "all_repos_updated": "All repositories updated",
        "please_select_workspace": "Please select a workspace first",
        "please_select_repo": "Please select a repository",
        "confirm_delete_workspace": "Are you sure you want to delete workspace",
        "confirm_remove_repo": "Are you sure you want to remove the following repositories",
        "this_will_not_delete_actual_files": "This will not delete the actual files",
        "note": "Note",
        "failed_to_get_branches": "Failed to get branches",
        "repo_imported": "Repository imported successfully",
        "batch_import_completed": "Batch import completed",
        "input_repo_url": "Enter repository URL",
        "clone_repo": "Clone Repository",
    },
    "zh": {
        "workspace": "工作空间",
        "add": "添加",
        "remove": "移除",
        "clone": "克隆",
        "import": "导入",
        "batch_import": "批量导入",
        "branch_action": "分支操作",
        "create_branch": "创建分支",
        "switch_branch": "切换分支",
        "merge_branch": "合并分支",
        "commit": "提交",
        "push": "推送",
        "pull": "拉取",
        "refresh": "刷新",
        "status": "状态",
        "settings": "设置",
        "language": "语言",
        "repo_name": "仓库名称",
        "current_branch": "当前分支",
        "untracked": "未跟踪",
        "last_commit": "最近提交",
        "error": "错误",
        "success": "成功",
        "info": "提示",
        "select_workspace": "请选择工作空间",
        "select_repo": "请选择仓库",
        "confirm_delete": "确认删除",
        "confirm_remove": "确认移除",
        "enter_commit_msg": "输入提交信息...",
        "changes_committed": "更改已提交",
        "changes_pushed": "更改已推送",
        "commit_msg_required": "请输入提交信息",
        "branch_name": "分支名称",
        "start_point": "起始点",
        "select_branch": "选择分支",
        "branch_created": "分支创建成功",
        "branch_switched": "分支切换成功",
        "branch_merged": "分支合并完成",
        "confirm": "确定",
        "cancel": "取消",
        "browse": "浏览",
        "path": "路径",
        "cbox_manager": "CBox 管理器",
        "workspace_name": "工作空间名称",
        "workspace_path": "工作空间路径",
        "input_workspace_name": "输入工作空间名称",
        "select_workspace_path": "选择工作空间路径",
        "select_workspace_directory": "选择工作空间目录",
        "input_branch_name": "输入分支名称",
        "optional_start_point": "可选，留空则从当前分支创建",
        "input_commit_message": "输入提交信息",
        "has_changes": "有更改",
        "clean": "干净",
        "no_commits": "无提交记录",
        "no_changes_to_commit": "没有需要提交的更改",
        "no_changes_to_push": "没有需要推送的更改",
        "all_repos_updated": "所有仓库已更新",
        "please_select_workspace": "请先选择一个工作空间",
        "please_select_repo": "请选择要操作的仓库",
        "confirm_delete_workspace": "确定要删除工作空间",
        "confirm_remove_repo": "确定要移除以下仓库",
        "this_will_not_delete_actual_files": "这不会删除实际的文件",
        "note": "注意",
        "failed_to_get_branches": "获取分支列表失败",
        "repo_imported": "仓库导入成功",
        "batch_import_completed": "批量导入完成",
        "input_repo_url": "输入仓库URL",
        "clone_repo": "克隆仓库",
    }
}

class LanguageManager:
    _instance = None
    _current_language = "zh"  # 默认中文

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def set_language(self, language):
        self._current_language = language

    def get_text(self, key):
        return TRANSLATIONS[self._current_language].get(key, key)

def tr(key):
    return LanguageManager.instance().get_text(key)
