#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 9：主窗口框架（QMainWindow）
目标：菜单栏、工具栏、状态栏
学习点：QMainWindow结构设计
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAction, QToolBar, QStatusBar, QLabel, QTextEdit
from PySide6.QtGui import QIcon, QKeySequence
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("主窗口框架示例")
        self.resize(600, 400)
        
        # 创建中央部件
        self.text_edit = QTextEdit()
        self.setCentralWidget(self.text_edit)
        
        # 创建菜单栏
        self.create_menu_bar()
        
        # 创建工具栏
        self.create_tool_bar()
        
        # 创建状态栏
        self.create_status_bar()
    
    def create_menu_bar(self):
        # 获取菜单栏
        menu_bar = self.menuBar()
        
        # 创建文件菜单
        file_menu = menu_bar.addMenu("文件")
        
        # 创建新建动作
        new_action = QAction("新建", self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(lambda: self.text_edit.clear())
        file_menu.addAction(new_action)
        
        # 创建打开动作
        open_action = QAction("打开", self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.show_status_message)
        file_menu.addAction(open_action)
        
        # 添加分隔线
        file_menu.addSeparator()
        
        # 创建退出动作
        exit_action = QAction("退出", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # 创建编辑菜单
        edit_menu = menu_bar.addMenu("编辑")
        
        # 创建复制动作
        copy_action = QAction("复制", self)
        copy_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)
        
        # 创建粘贴动作
        paste_action = QAction("粘贴", self)
        paste_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)
    
    def create_tool_bar(self):
        # 创建工具栏
        tool_bar = QToolBar("主工具栏")
        self.addToolBar(tool_bar)
        
        # 创建清除动作
        clear_action = QAction("清除", self)
        clear_action.triggered.connect(self.text_edit.clear)
        tool_bar.addAction(clear_action)
        
        # 创建字体加粗动作
        bold_action = QAction("加粗", self)
        bold_action.setCheckable(True)
        bold_action.triggered.connect(self.toggle_bold)
        tool_bar.addAction(bold_action)
    
    def create_status_bar(self):
        # 创建状态栏
        status_bar = QStatusBar()
        self.setStatusBar(status_bar)
        
        # 添加永久消息
        status_bar.addPermanentWidget(QLabel("就绪"))
    
    def show_status_message(self):
        # 在状态栏显示临时消息
        self.statusBar().showMessage("打开文件操作被触发", 2000)  # 显示2秒
    
    def toggle_bold(self, checked):
        # 切换文本加粗
        font = self.text_edit.font()
        font.setBold(checked)
        self.text_edit.setFont(font)


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建主窗口
    window = MainWindow()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()