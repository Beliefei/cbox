#!/usr/bin/env python3
import sys
import os

# 确保能够正确导入 cbox 模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from cbox.gui import CBoxGUI
from PySide6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    window = CBoxGUI()
    window.show()
    sys.exit(app.exec())
