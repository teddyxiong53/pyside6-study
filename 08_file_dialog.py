#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 8：文件选择对话框
目标：文件读写操作
学习点：QFileDialog、文件路径处理
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QTextEdit


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("文件选择对话框示例")
    window.resize(500, 400)
    
    # 创建布局
    layout = QVBoxLayout()
    
    # 创建标签显示选择的文件路径
    path_label = QLabel("未选择文件")
    layout.addWidget(path_label)
    
    # 创建文本编辑框显示文件内容
    text_edit = QTextEdit()
    layout.addWidget(text_edit)
    
    # 创建打开文件按钮
    open_button = QPushButton("打开文件")
    open_button.clicked.connect(lambda: open_file(window, path_label, text_edit))
    layout.addWidget(open_button)
    
    # 创建保存文件按钮
    save_button = QPushButton("保存文件")
    save_button.clicked.connect(lambda: save_file(window, text_edit))
    layout.addWidget(save_button)
    
    # 设置窗口布局
    window.setLayout(layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


def open_file(window, path_label, text_edit):
    # 打开文件对话框
    file_path, _ = QFileDialog.getOpenFileName(
        window,
        "选择文件",
        "",
        "文本文件 (*.txt);;Python文件 (*.py);;所有文件 (*)"
    )
    
    # 如果选择了文件
    if file_path:
        path_label.setText(f"已选择文件: {file_path}")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text_edit.setText(file.read())
        except Exception as e:
            path_label.setText(f"读取文件出错: {str(e)}")


def save_file(window, text_edit):
    # 保存文件对话框
    file_path, _ = QFileDialog.getSaveFileName(
        window,
        "保存文件",
        "",
        "文本文件 (*.txt);;Python文件 (*.py);;所有文件 (*)"
    )
    
    # 如果选择了保存路径
    if file_path:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text_edit.toPlainText())
        except Exception as e:
            print(f"保存文件出错: {str(e)}")


if __name__ == "__main__":
    main()