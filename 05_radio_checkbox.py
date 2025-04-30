#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 5：单选按钮与复选框
目标：处理多选项逻辑
学习点：QRadioButton、QCheckBox状态监听
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QRadioButton, QCheckBox, QButtonGroup, QLabel


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("单选按钮与复选框")
    window.resize(400, 300)
    
    # 创建布局
    layout = QVBoxLayout()
    
    # 添加标签
    layout.addWidget(QLabel("单选按钮示例："))
    
    # 创建单选按钮组
    radio_group = QButtonGroup(window)
    
    # 创建单选按钮
    radio1 = QRadioButton("选项1")
    radio2 = QRadioButton("选项2")
    radio3 = QRadioButton("选项3")
    
    # 添加到按钮组
    radio_group.addButton(radio1, 1)
    radio_group.addButton(radio2, 2)
    radio_group.addButton(radio3, 3)
    
    # 添加到布局
    layout.addWidget(radio1)
    layout.addWidget(radio2)
    layout.addWidget(radio3)
    
    # 添加标签
    layout.addWidget(QLabel("复选框示例："))
    
    # 创建复选框
    checkbox1 = QCheckBox("同意协议")
    checkbox2 = QCheckBox("接收通知")
    
    # 状态变更事件
    status_label = QLabel("状态：未选择")
    checkbox1.stateChanged.connect(lambda state: status_label.setText(f"状态：{'已选择' if state else '未选择'}"))
    
    # 添加到布局
    layout.addWidget(checkbox1)
    layout.addWidget(checkbox2)
    layout.addWidget(status_label)
    
    # 设置窗口布局
    window.setLayout(layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()