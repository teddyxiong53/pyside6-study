#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 10：多标签界面（QTabWidget）
目标：多页面切换
学习点：多标签管理
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit


class TabDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("多标签界面示例")
        self.resize(500, 400)
        
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建标签控件
        self.tab_widget = QTabWidget()
        
        # 创建第一个标签页
        self.tab1 = QWidget()
        self.create_tab1()
        
        # 创建第二个标签页
        self.tab2 = QWidget()
        self.create_tab2()
        
        # 创建第三个标签页
        self.tab3 = QWidget()
        self.create_tab3()
        
        # 添加标签页到标签控件
        self.tab_widget.addTab(self.tab1, "表单")
        self.tab_widget.addTab(self.tab2, "文本编辑")
        self.tab_widget.addTab(self.tab3, "按钮")
        
        # 添加标签控件到主布局
        main_layout.addWidget(self.tab_widget)
        
        # 设置窗口布局
        self.setLayout(main_layout)
    
    def create_tab1(self):
        # 创建表单布局
        layout = QVBoxLayout()
        
        # 添加表单元素
        layout.addWidget(QLabel("姓名："))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("年龄："))
        layout.addWidget(QLineEdit())
        layout.addWidget(QLabel("地址："))
        layout.addWidget(QLineEdit())
        
        # 添加提交按钮
        submit_button = QPushButton("提交")
        layout.addWidget(submit_button)
        
        # 设置标签页布局
        self.tab1.setLayout(layout)
    
    def create_tab2(self):
        # 创建文本编辑布局
        layout = QVBoxLayout()
        
        # 添加文本编辑控件
        text_edit = QTextEdit()
        layout.addWidget(text_edit)
        
        # 设置标签页布局
        self.tab2.setLayout(layout)
    
    def create_tab3(self):
        # 创建按钮布局
        layout = QVBoxLayout()
        
        # 添加多个按钮
        for i in range(1, 6):
            button = QPushButton(f"按钮 {i}")
            layout.addWidget(button)
        
        # 设置标签页布局
        self.tab3.setLayout(layout)


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = TabDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()