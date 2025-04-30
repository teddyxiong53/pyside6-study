#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 14：事件过滤器
目标：全局事件拦截
学习点：事件监听与过滤机制
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PySide6.QtCore import QObject, QEvent, Qt


class EventFilterDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("事件过滤器示例")
        self.resize(500, 400)
        
        # 创建UI
        self.init_ui()
        
        # 安装事件过滤器
        self.install_event_filters()
    
    def init_ui(self):
        # 创建主布局
        layout = QVBoxLayout()
        
        # 创建标签
        self.info_label = QLabel("鼠标和键盘事件将显示在下方")
        layout.addWidget(self.info_label)
        
        # 创建按钮
        self.button = QPushButton("点击我或悬停在我上面")
        layout.addWidget(self.button)
        
        # 创建文本编辑框
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("在此输入文本，键盘事件将被捕获")
        layout.addWidget(self.text_edit)
        
        # 创建事件日志
        self.log = QTextEdit()
        self.log.setReadOnly(True)
        self.log.setPlaceholderText("事件日志将显示在这里")
        layout.addWidget(self.log)
        
        # 设置窗口布局
        self.setLayout(layout)
    
    def install_event_filters(self):
        # 为按钮安装事件过滤器
        self.button.installEventFilter(self)
        
        # 为文本编辑框安装事件过滤器
        self.text_edit.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        # 过滤按钮事件
        if obj is self.button:
            if event.type() == QEvent.Enter:
                self.log_event("鼠标进入按钮")
                self.button.setStyleSheet("background-color: #4CAF50; color: white;")
            elif event.type() == QEvent.Leave:
                self.log_event("鼠标离开按钮")
                self.button.setStyleSheet("")
            elif event.type() == QEvent.MouseButtonPress:
                self.log_event("鼠标按下按钮")
        
        # 过滤文本编辑框事件
        elif obj is self.text_edit:
            if event.type() == QEvent.KeyPress:
                key = event.key()
                if key == Qt.Key_Return or key == Qt.Key_Enter:
                    self.log_event("按下回车键")
                elif key == Qt.Key_Escape:
                    self.log_event("按下ESC键")
                else:
                    self.log_event(f"按下键: {event.text()}")
        
        # 继续传递事件给父类处理
        return super().eventFilter(obj, event)
    
    def log_event(self, message):
        # 在日志中添加事件信息
        self.log.append(message)


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = EventFilterDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()