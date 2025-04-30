#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 13：样式表美化（QSS）
目标：自定义控件外观
学习点：CSS语法与样式继承
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QCheckBox, QGroupBox


class StyleSheetDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("样式表美化示例")
        self.resize(500, 400)
        
        # 创建UI
        self.init_ui()
        
        # 应用样式表
        self.apply_stylesheet()
    
    def init_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建标题标签
        title_label = QLabel("样式表美化示例")
        title_label.setObjectName("titleLabel")
        main_layout.addWidget(title_label)
        
        # 创建表单组
        form_group = QGroupBox("表单样式")
        form_group.setObjectName("formGroup")
        form_layout = QVBoxLayout()
        
        # 添加输入框
        name_input = QLineEdit()
        name_input.setPlaceholderText("请输入用户名")
        form_layout.addWidget(name_input)
        
        # 添加下拉框
        combo_box = QComboBox()
        combo_box.addItems(["选项1", "选项2", "选项3"])
        form_layout.addWidget(combo_box)
        
        # 添加复选框
        checkbox = QCheckBox("同意协议")
        form_layout.addWidget(checkbox)
        
        # 设置表单组布局
        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)
        
        # 创建按钮组
        button_group = QGroupBox("按钮样式")
        button_group.setObjectName("buttonGroup")
        button_layout = QVBoxLayout()
        
        # 添加普通按钮
        normal_button = QPushButton("普通按钮")
        button_layout.addWidget(normal_button)
        
        # 添加主要按钮
        primary_button = QPushButton("主要按钮")
        primary_button.setObjectName("primaryButton")
        button_layout.addWidget(primary_button)
        
        # 添加危险按钮
        danger_button = QPushButton("危险按钮")
        danger_button.setObjectName("dangerButton")
        button_layout.addWidget(danger_button)
        
        # 设置按钮组布局
        button_group.setLayout(button_layout)
        main_layout.addWidget(button_group)
        
        # 设置窗口布局
        self.setLayout(main_layout)
    
    def apply_stylesheet(self):
        # 定义样式表
        self.setStyleSheet("""
            /* 全局样式 */
            QWidget {
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            
            /* 标题样式 */
            #titleLabel {
                font-size: 24px;
                font-weight: bold;
                color: #333;
                margin: 10px 0;
            }
            
            /* 表单组样式 */
            #formGroup {
                background-color: #f5f5f5;
                border-radius: 8px;
                padding: 10px;
                margin: 5px 0;
            }
            
            /* 输入框样式 */
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
            }
            
            QLineEdit:focus {
                border-color: #4CAF50;
            }
            
            /* 下拉框样式 */
            QComboBox {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
            }
            
            /* 复选框样式 */
            QCheckBox {
                spacing: 8px;
            }
            
            /* 按钮组样式 */
            #buttonGroup {
                background-color: #e9e9e9;
                border-radius: 8px;
                padding: 10px;
                margin: 5px 0;
            }
            
            /* 按钮通用样式 */
            QPushButton {
                padding: 10px;
                border: none;
                border-radius: 5px;
                background-color: #ddd;
                color: #333;
                min-height: 30px;
            }
            
            QPushButton:hover {
                background-color: #ccc;
            }
            
            /* 主要按钮样式 */
            #primaryButton {
                background-color: #4CAF50;
                color: white;
            }
            
            #primaryButton:hover {
                background-color: #45a049;
            }
            
            /* 危险按钮样式 */
            #dangerButton {
                background-color: #f44336;
                color: white;
            }
            
            #dangerButton:hover {
                background-color: #d32f2f;
            }
        """)


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = StyleSheetDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()