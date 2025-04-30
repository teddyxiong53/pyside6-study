#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 11：表格数据展示（QTableView）
目标：模型-视图架构
学习点：自定义模型与视图绑定
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QPushButton, QHBoxLayout
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["ID", "姓名", "年龄", "职业"]
    
    def rowCount(self, parent=QModelIndex()):
        # 返回行数
        return len(self._data)
    
    def columnCount(self, parent=QModelIndex()):
        # 返回列数
        return len(self._headers)
    
    def data(self, index, role=Qt.DisplayRole):
        # 返回数据
        if not index.isValid():
            return None
        
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        
        return None
    
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        # 返回表头数据
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            else:
                return str(section + 1)
        
        return None
    
    def flags(self, index):
        # 设置单元格标志
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable


class TableViewDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("表格数据展示示例")
        self.resize(600, 400)
        
        # 创建布局
        layout = QVBoxLayout()
        
        # 创建表格视图
        self.table_view = QTableView()
        
        # 准备数据
        self.data = [
            [1, "张三", 28, "工程师"],
            [2, "李四", 32, "设计师"],
            [3, "王五", 45, "经理"],
            [4, "赵六", 36, "销售"],
            [5, "钱七", 25, "程序员"]
        ]
        
        # 创建模型并设置到视图
        self.model = TableModel(self.data)
        self.table_view.setModel(self.model)
        
        # 调整列宽以适应内容
        self.table_view.resizeColumnsToContents()
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        
        # 添加刷新按钮
        refresh_button = QPushButton("刷新数据")
        refresh_button.clicked.connect(self.refresh_data)
        button_layout.addWidget(refresh_button)
        
        # 添加控件到布局
        layout.addWidget(self.table_view)
        layout.addLayout(button_layout)
        
        # 设置窗口布局
        self.setLayout(layout)
    
    def refresh_data(self):
        # 更新数据（这里只是简单地修改年龄）
        for row in self.data:
            row[2] += 1
        
        # 通知模型数据已更改
        self.model.layoutChanged.emit()
        
        # 调整列宽
        self.table_view.resizeColumnsToContents()


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = TableViewDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()