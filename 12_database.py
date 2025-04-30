#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 12：数据库连接（SQLite）
目标：GUI与数据库交互
学习点：sqlite3集成与CRUD操作
"""

import sys
import sqlite3
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit, QLabel, QMessageBox


class DatabaseDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("数据库连接示例")
        self.resize(600, 400)
        
        # 创建数据库连接
        self.create_database()
        
        # 创建UI
        self.init_ui()
        
        # 加载数据
        self.load_data()
    
    def create_database(self):
        # 连接到SQLite数据库（如果不存在则创建）
        self.conn = sqlite3.connect("data.db")
        self.cursor = self.conn.cursor()
        
        # 创建用户表（如果不存在）
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        
        # 提交更改
        self.conn.commit()
    
    def init_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建表单布局
        form_layout = QHBoxLayout()
        
        # 添加输入框
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("姓名")
        form_layout.addWidget(QLabel("姓名:"))
        form_layout.addWidget(self.name_input)
        
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("邮箱")
        form_layout.addWidget(QLabel("邮箱:"))
        form_layout.addWidget(self.email_input)
        
        # 添加按钮
        add_button = QPushButton("添加")
        add_button.clicked.connect(self.add_user)
        form_layout.addWidget(add_button)
        
        # 创建表格
        self.table = QTableWidget(0, 3)  # 0行3列
        self.table.setHorizontalHeaderLabels(["ID", "姓名", "邮箱"])
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        
        # 添加删除按钮
        delete_button = QPushButton("删除所选")
        delete_button.clicked.connect(self.delete_user)
        button_layout.addWidget(delete_button)
        
        # 添加刷新按钮
        refresh_button = QPushButton("刷新")
        refresh_button.clicked.connect(self.load_data)
        button_layout.addWidget(refresh_button)
        
        # 添加控件到主布局
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.table)
        main_layout.addLayout(button_layout)
        
        # 设置窗口布局
        self.setLayout(main_layout)
    
    def load_data(self):
        # 清空表格
        self.table.setRowCount(0)
        
        # 查询所有用户
        self.cursor.execute("SELECT id, name, email FROM users")
        users = self.cursor.fetchall()
        
        # 填充表格
        for row_index, user in enumerate(users):
            self.table.insertRow(row_index)
            for col_index, value in enumerate(user):
                self.table.setItem(row_index, col_index, QTableWidgetItem(str(value)))
        
        # 调整列宽
        self.table.resizeColumnsToContents()
    
    def add_user(self):
        # 获取输入
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        
        # 验证输入
        if not name or not email:
            QMessageBox.warning(self, "输入错误", "姓名和邮箱不能为空！")
            return
        
        try:
            # 插入数据
            self.cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (name, email)
            )
            
            # 提交更改
            self.conn.commit()
            
            # 清空输入框
            self.name_input.clear()
            self.email_input.clear()
            
            # 重新加载数据
            self.load_data()
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"添加用户失败: {str(e)}")
    
    def delete_user(self):
        # 获取选中的行
        selected_rows = self.table.selectedItems()
        if not selected_rows:
            QMessageBox.information(self, "提示", "请先选择要删除的用户")
            return
        
        # 获取用户ID
        row = selected_rows[0].row()
        user_id = self.table.item(row, 0).text()
        
        try:
            # 删除数据
            self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            
            # 提交更改
            self.conn.commit()
            
            # 重新加载数据
            self.load_data()
            
        except Exception as e:
            QMessageBox.critical(self, "错误", f"删除用户失败: {str(e)}")
    
    def closeEvent(self, event):
        # 关闭数据库连接
        if hasattr(self, 'conn'):
            self.conn.close()
        event.accept()


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = DatabaseDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()