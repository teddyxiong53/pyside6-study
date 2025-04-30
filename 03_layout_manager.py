#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 3：布局管理器（垂直/水平布局）
目标：使用QVBoxLayout和QHBoxLayout
学习点：布局管理器实现控件自动排列
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = QWidget()
    window.setWindowTitle("布局管理器示例")
    window.resize(400, 300)
    
    # 创建垂直布局
    v_layout = QVBoxLayout()
    v_layout.addWidget(QLabel("垂直布局示例"))
    v_layout.addWidget(QPushButton("按钮1"))
    v_layout.addWidget(QPushButton("按钮2"))
    
    # 创建水平布局
    h_layout = QHBoxLayout()
    h_layout.addWidget(QLabel("水平布局："))
    h_layout.addWidget(QPushButton("按钮3"))
    h_layout.addWidget(QPushButton("按钮4"))
    
    # 将水平布局添加到垂直布局中
    v_layout.addLayout(h_layout)
    
    # 设置窗口布局
    window.setLayout(v_layout)
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()