
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

