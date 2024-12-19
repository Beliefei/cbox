#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

def run_command(cmd):
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)

def build_app():
    # 确保我们在正确的目录
    project_root = Path(__file__).parent.absolute()
    os.chdir(project_root)

    # 安装依赖
    print("Installing requirements...")
    run_command([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    run_command([sys.executable, "-m", "pip", "install", "pyinstaller"])

    # 创建 .spec 文件
    spec_content = """
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['cbox_app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'PySide6.QtXml',
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'yaml',
        'git',
        'rich',
        'click'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PyQt5', 'PyQt6', 'PyQt4'],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# 添加数据文件
a.datas += [
    ('cbox/i18n.py', 'cbox/i18n.py', 'DATA'),
]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CBox',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=True,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CBox',
)

app = BUNDLE(
    coll,
    name='CBox.app',
    icon='cbox.icns',
    bundle_identifier='com.belief.cbox',
    version='0.1.6',
    info_plist={
        'NSHighResolutionCapable': 'True',
        'LSBackgroundOnly': 'False',
        'NSRequiresAquaSystemAppearance': 'False',
        'CFBundleName': 'CBox',
        'CFBundleDisplayName': 'CBox',
        'CFBundleGetInfoString': 'Multi-repository management tool',
        'CFBundleIdentifier': 'com.belief.cbox',
        'CFBundleVersion': '0.1.6',
        'CFBundleShortVersionString': '0.1.6',
        'NSHumanReadableCopyright': ' 2024 belief. All rights reserved.',
        'LSMinimumSystemVersion': '10.13.0',
        'NSPrincipalClass': 'NSApplication',
        'NSAppleScriptEnabled': False,
        'CFBundleDocumentTypes': [{
            'CFBundleTypeName': 'CBox Workspace',
            'CFBundleTypeRole': 'Editor',
            'LSHandlerRank': 'Owner'
        }],
    },
)

"""
    # 写入 .spec 文件
    spec_file = project_root / "CBox.spec"
    spec_file.write_text(spec_content)

    # 清理之前的构建
    print("Cleaning previous build...")
    dist_dir = project_root / "dist"
    build_dir = project_root / "build"
    if dist_dir.exists():
        run_command(["rm", "-rf", str(dist_dir)])
    if build_dir.exists():
        run_command(["rm", "-rf", str(build_dir)])

    # 使用 PyInstaller 构建应用
    print("Building application...")
    run_command(["pyinstaller", "--clean", "CBox.spec"])

    print("\nBuild complete!")
    print(f"You can find the application at: {project_root}/dist/CBox.app")

if __name__ == "__main__":
    build_app()
