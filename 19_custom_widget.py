#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 19：自定义控件
目标：继承QWidget扩展功能
学习点：控件继承与重写
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider
from PySide6.QtCore import Qt, Signal, Property
from PySide6.QtGui import QPainter, QColor, QPen, QFont


class ColorButton(QPushButton):
    """自定义彩色按钮控件"""
    
    def __init__(self, text, color="#FF5722", parent=None):
        super().__init__(text, parent)
        self.setColor(color)
        self.setMinimumHeight(40)
    
    def setColor(self, color):
        self._color = QColor(color)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 16px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {QColor(color).darker(110).name()};
            }}
            QPushButton:pressed {{
                background-color: {QColor(color).darker(120).name()};
            }}
        """)


class RatingWidget(QWidget):
    """自定义评分控件"""
    
    # 定义信号
    ratingChanged = Signal(int)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._rating = 0
        self._max_rating = 5
        self._star_size = 30
        self.setMouseTracking(True)
        self.setMinimumSize(self._max_rating * self._star_size, self._star_size)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # 绘制星星
        for i in range(self._max_rating):
            if i < self._rating:
                # 填充的星星
                painter.setPen(QPen(Qt.darkYellow))
                painter.setBrush(QColor(255, 215, 0))  # 金色
            else:
                # 空心的星星
                painter.setPen(QPen(Qt.gray))
                painter.setBrush(Qt.transparent)
            
            # 绘制星形（简化为矩形）
            x = i * self._star_size
            painter.drawRect(x, 0, self._star_size - 2, self._star_size - 2)
            
            # 绘制星号文本
            painter.setFont(QFont("Arial", 16, QFont.Bold))
            painter.drawText(x, 0, self._star_size, self._star_size, Qt.AlignCenter, "★")
    
    def mouseMoveEvent(self, event):
        # 根据鼠标位置计算评分
        x = event.position().x()
        new_rating = min(max(int(x / self._star_size) + 1, 1), self._max_rating)
        
        if new_rating != self._rating:
            self._rating = new_rating
            self.update()
    
    def mouseReleaseEvent(self, event):
        # 鼠标释放时发出信号
        self.ratingChanged.emit(self._rating)
    
    def getRating(self):
        return self._rating
    
    def setRating(self, rating):
        if 0 <= rating <= self._max_rating and rating != self._rating:
            self._rating = rating
            self.update()
            self.ratingChanged.emit(rating)
    
    # 定义属性
    rating = Property(int, getRating, setRating)


class ProgressButton(QWidget):
    """带进度条的按钮控件"""
    
    clicked = Signal()
    
    def __init__(self, text="Progress Button", parent=None):
        super().__init__(parent)
        self._progress = 0
        self._text = text
        
        # 创建布局
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建按钮
        self.button = QPushButton(text)
        self.button.clicked.connect(self.clicked)
        layout.addWidget(self.button)
        
        # 创建进度条
        self.progress_bar = QSlider(Qt.Horizontal)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setEnabled(False)
        layout.addWidget(self.progress_bar)
        
        # 设置布局
        self.setLayout(layout)
    
    def setProgress(self, value):
        self._progress = max(0, min(100, value))
        self.progress_bar.setValue(self._progress)
    
    def getProgress(self):
        return self._progress
    
    # 定义属性
    progress = Property(int, getProgress, setProgress)


class CustomWidgetDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("自定义控件示例")
        self.resize(500, 400)
        
        # 创建UI
        self.init_ui()
    
    def init_ui(self):
        # 创建主布局
        layout = QVBoxLayout()
        
        # 添加标题
        title = QLabel("自定义控件示例")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(title)
        
        # 添加自定义彩色按钮
        layout.addWidget(QLabel("自定义彩色按钮:"))
        button_layout = QHBoxLayout()
        button_layout.addWidget(ColorButton("红色按钮", "#F44336"))
        button_layout.addWidget(ColorButton("绿色按钮", "#4CAF50"))
        button_layout.addWidget(ColorButton("蓝色按钮", "#2196F3"))
        layout.addLayout(button_layout)
        
        # 添加自定义评分控件
        layout.addWidget(QLabel("自定义评分控件:"))
        self.rating_widget = RatingWidget()
        self.rating_label = QLabel("当前评分: 0")
        self.rating_widget.ratingChanged.connect(lambda rating: self.rating_label.setText(f"当前评分: {rating}"))
        layout.addWidget(self.rating_widget)
        layout.addWidget(self.rating_label)
        
        # 添加自定义进度按钮
        layout.addWidget(QLabel("自定义进度按钮:"))
        self.progress_button = ProgressButton("点击增加进度")
        self.progress_button.clicked.connect(self.increase_progress)
        layout.addWidget(self.progress_button)
        
        # 设置窗口布局
        self.setLayout(layout)
    
    def increase_progress(self):
        # 增加进度
        current = self.progress_button.progress
        if current < 100:
            self.progress_button.setProgress(current + 10)


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = CustomWidgetDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()