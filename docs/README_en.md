# CBox

CBox is a powerful multi-repository management tool that helps you better organize and manage multiple Git repositories. It supports workspace management, batch operations, branch management, and other features, making multi-repository management simple and efficient.

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
git clone https://github.com/beliefei/cbox.git
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

For more information, visit our [GitHub repository](https://github.com/beliefei/cbox).
