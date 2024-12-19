from setuptools import setup, find_packages

setup(
    name="cbox-tool",
    version="0.1.12",
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

[English](https://github.com/Beliefei/cbox/docs/README_en.md) | [中文](https://github.com/Beliefei/cbox/docs/README_zh.md)

<div align="center">

![CBox Logo](https://github.com/Beliefei/cbox/blob/main/icon.png)

A powerful multi-repository management tool with GUI support.

[![PyPI version](https://badge.fury.io/py/cbox-tool.svg)](https://badge.fury.io/py/cbox-tool)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

**English** | [中文](https://github.com/Beliefei/cbox/docs/README_zh.md)

CBox is a powerful multi-repository management tool that helps you better organize and manage multiple Git repositories. It supports workspace management, batch operations, branch management, and other features, making multi-repository management simple and efficient.

## Features
- Multi-repository management
- Workspace organization
- Batch operations for Git commands
- Branch management and switching
- User-friendly GUI

## Installation
You can install CBox using pip:

```bash
pip install cbox-tool
```

## Usage
After installation, you can run CBox using the following command:

```bash
cbox-gui
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License.
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
