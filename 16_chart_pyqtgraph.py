#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 16：图表绘制（PyQtGraph）
目标：动态数据可视化
学习点：集成第三方图表库
"""

import sys
import numpy as np
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QComboBox, QLabel
import pyqtgraph as pg


class ChartDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("图表绘制示例")
        self.resize(800, 500)
        
        # 创建UI
        self.init_ui()
        
        # 初始化数据
        self.init_data()
    
    def init_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建图表控件
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.setBackground('w')  # 白色背景
        self.plot_widget.showGrid(x=True, y=True)
        self.plot_widget.setLabel('left', "值")
        self.plot_widget.setLabel('bottom', "时间")
        self.plot_widget.addLegend()
        
        # 添加图表控件到布局
        main_layout.addWidget(self.plot_widget)
        
        # 创建控制面板
        control_layout = QHBoxLayout()
        
        # 添加图表类型选择
        control_layout.addWidget(QLabel("图表类型:"))
        self.chart_type = QComboBox()
        self.chart_type.addItems(["折线图", "柱状图", "散点图"])
        self.chart_type.currentIndexChanged.connect(self.update_chart)
        control_layout.addWidget(self.chart_type)
        
        # 添加数据更新按钮
        self.update_button = QPushButton("更新数据")
        self.update_button.clicked.connect(self.generate_new_data)
        control_layout.addWidget(self.update_button)
        
        # 添加控制面板到主布局
        main_layout.addLayout(control_layout)
        
        # 设置窗口布局
        self.setLayout(main_layout)
    
    def init_data(self):
        # 初始化数据
        self.x = np.arange(100)
        self.y1 = np.sin(self.x / 10) * 3
        self.y2 = np.cos(self.x / 10) * 2
        
        # 绘制初始图表
        self.update_chart()
    
    def update_chart(self, index=0):
        # 清除图表
        self.plot_widget.clear()
        
        # 根据选择的图表类型绘制
        chart_type = self.chart_type.currentText() if hasattr(self, 'chart_type') else "折线图"
        
        if chart_type == "折线图":
            # 绘制折线图
            self.plot_widget.plot(self.x, self.y1, pen=pg.mkPen(color='b', width=2), name="Sin")
            self.plot_widget.plot(self.x, self.y2, pen=pg.mkPen(color='r', width=2), name="Cos")
        
        elif chart_type == "柱状图":
            # 绘制柱状图（使用BarGraphItem）
            bg1 = pg.BarGraphItem(x=self.x[::5], height=self.y1[::5], width=0.8, brush='b')
            bg2 = pg.BarGraphItem(x=self.x[::5]+0.4, height=self.y2[::5], width=0.8, brush='r')
            self.plot_widget.addItem(bg1)
            self.plot_widget.addItem(bg2)
        
        elif chart_type == "散点图":
            # 绘制散点图
            scatter1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(0, 0, 255, 120))
            scatter2 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 0, 0, 120))
            scatter1.addPoints(self.x, self.y1)
            scatter2.addPoints(self.x, self.y2)
            self.plot_widget.addItem(scatter1)
            self.plot_widget.addItem(scatter2)
    
    def generate_new_data(self):
        # 生成新数据
        phase = np.random.random() * 10
        self.y1 = np.sin((self.x + phase) / 10) * 3
        self.y2 = np.cos((self.x + phase) / 10) * 2
        
        # 更新图表
        self.update_chart()


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = ChartDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()