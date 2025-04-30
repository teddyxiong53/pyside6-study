#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 1：创建第一个窗口
目标：掌握窗口创建与事件循环
学习点：QApplication、QWidget、事件循环机制
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("Hello PySide6")
    window.resize(400, 300)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()