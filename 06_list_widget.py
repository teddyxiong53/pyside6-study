#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 6：列表控件（QListWidget）
目标：动态管理列表项
学习点：列表项的增删与事件绑定
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QPushButton, QHBoxLayout, QLineEdit, QLabel


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("列表控件示例")
    window.resize(400, 300)
    
    # 创建主布局
    main_layout = QVBoxLayout()
    
    # 创建列表控件
    list_widget = QListWidget()
    list_widget.addItems(["Item 1", "Item 2", "Item 3"])
    
    # 创建标签显示选中项
    selected_label = QLabel("选中：无")
    
    # 连接信号与槽
    list_widget.itemClicked.connect(lambda item: selected_label.setText(f"选中：{item.text()}"))
    
    # 创建输入框和按钮的水平布局
    input_layout = QHBoxLayout()
    item_input = QLineEdit()
    item_input.setPlaceholderText("输入新项目")
    add_button = QPushButton("添加")
    remove_button = QPushButton("删除选中项")
    
    # 添加按钮点击事件
    add_button.clicked.connect(lambda: list_widget.addItem(item_input.text()) if item_input.text() else None)
    # 删除按钮点击事件
    remove_button.clicked.connect(lambda: list_widget.takeItem(list_widget.currentRow()) if list_widget.currentRow() >= 0 else None)
    
    # 添加控件到水平布局
    input_layout.addWidget(item_input)
    input_layout.addWidget(add_button)
    input_layout.addWidget(remove_button)
    
    # 添加控件到主布局
    main_layout.addWidget(list_widget)
    main_layout.addLayout(input_layout)
    main_layout.addWidget(selected_label)
    
    # 设置窗口布局
    window.setLayout(main_layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()