#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 7：消息对话框
目标：弹窗交互设计
学习点：QMessageBox的多种类型（信息、警告、提问）
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("消息对话框示例")
    window.resize(400, 300)
    
    # 创建布局
    layout = QVBoxLayout()
    
    # 创建信息对话框按钮
    info_button = QPushButton("显示信息对话框")
    info_button.clicked.connect(lambda: QMessageBox.information(window, "信息", "这是一个信息对话框"))
    layout.addWidget(info_button)
    
    # 创建警告对话框按钮
    warning_button = QPushButton("显示警告对话框")
    warning_button.clicked.connect(lambda: QMessageBox.warning(window, "警告", "这是一个警告对话框"))
    layout.addWidget(warning_button)
    
    # 创建错误对话框按钮
    error_button = QPushButton("显示错误对话框")
    error_button.clicked.connect(lambda: QMessageBox.critical(window, "错误", "这是一个错误对话框"))
    layout.addWidget(error_button)
    
    # 创建问题对话框按钮
    question_button = QPushButton("显示问题对话框")
    question_button.clicked.connect(show_question_dialog)
    layout.addWidget(question_button)
    
    # 设置窗口布局
    window.setLayout(layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


def show_question_dialog():
    # 显示问题对话框
    reply = QMessageBox.question(
        None, 
        "确认", 
        "确定要退出吗？", 
        QMessageBox.Yes | QMessageBox.No, 
        QMessageBox.No
    )
    
    # 处理用户选择
    if reply == QMessageBox.Yes:
        print("用户选择了'是'")
    else:
        print("用户选择了'否'")


if __name__ == "__main__":
    main()