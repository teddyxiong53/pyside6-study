#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 2：按钮与信号槽
目标：理解信号与槽机制
学习点：QPushButton、clicked信号、匿名函数槽
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QVBoxLayout


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("按钮与信号槽")
    window.resize(300, 200)
    
    # 创建布局
    layout = QVBoxLayout()
    
    # 创建按钮
    button = QPushButton("点击我", window)
    # 连接信号与槽
    button.clicked.connect(lambda: QMessageBox.information(window, "提示", "按钮被点击！"))
    
    # 添加按钮到布局
    layout.addWidget(button)
    
    # 设置窗口布局
    window.setLayout(layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()