#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 4：输入框与标签交互
目标：处理用户输入
学习点：QLineEdit、textChanged信号
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("输入框与标签交互")
    window.resize(400, 200)
    
    # 创建布局
    layout = QVBoxLayout()
    
    # 创建标签
    label = QLabel("输入内容：")
    layout.addWidget(label)
    
    # 创建输入框
    line_edit = QLineEdit()
    # 连接信号与槽
    line_edit.textChanged.connect(lambda text: label.setText(f"输入内容：{text}"))
    layout.addWidget(line_edit)
    
    # 设置窗口布局
    window.setLayout(layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()