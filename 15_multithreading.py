#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 15：多线程任务
目标：防止界面卡顿
学习点：QThread与信号通信
"""

import sys
import time
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QProgressBar, QLabel
from PySide6.QtCore import QThread, Signal


class Worker(QThread):
    # 定义信号
    progress = Signal(int)
    finished = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_running = True
    
    def run(self):
        # 模拟耗时任务
        for i in range(101):
            if not self.is_running:
                break
            
            # 发送进度信号
            self.progress.emit(i)
            
            # 模拟耗时操作
            time.sleep(0.1)
        
        # 发送完成信号
        self.finished.emit()
    
    def stop(self):
        self.is_running = False


class ThreadingDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("多线程任务示例")
        self.resize(500, 300)
        
        # 创建UI
        self.init_ui()
        
        # 初始化工作线程
        self.worker = None
    
    def init_ui(self):
        # 创建主布局
        layout = QVBoxLayout()
        
        # 创建标签
        self.status_label = QLabel("点击开始按钮执行耗时任务")
        layout.addWidget(self.status_label)
        
        # 创建进度条
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        
        # 创建按钮
        self.start_button = QPushButton("开始任务")
        self.start_button.clicked.connect(self.start_task)
        layout.addWidget(self.start_button)
        
        self.stop_button = QPushButton("停止任务")
        self.stop_button.clicked.connect(self.stop_task)
        self.stop_button.setEnabled(False)
        layout.addWidget(self.stop_button)
        
        # 创建演示按钮（证明UI不会卡顿）
        self.demo_button = QPushButton("点击我测试UI响应")
        self.demo_button.clicked.connect(self.show_response)
        layout.addWidget(self.demo_button)
        
        # 设置窗口布局
        self.setLayout(layout)
    
    def start_task(self):
        # 创建工作线程
        self.worker = Worker()
        
        # 连接信号
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.task_finished)
        
        # 更新UI状态
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.status_label.setText("任务执行中...")
        
        # 启动线程
        self.worker.start()
    
    def stop_task(self):
        # 停止工作线程
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.status_label.setText("任务已停止")
            self.stop_button.setEnabled(False)
            self.start_button.setEnabled(True)
    
    def update_progress(self, value):
        # 更新进度条
        self.progress_bar.setValue(value)
    
    def task_finished(self):
        # 任务完成后更新UI
        self.status_label.setText("任务已完成")
        self.stop_button.setEnabled(False)
        self.start_button.setEnabled(True)
    
    def show_response(self):
        # 证明UI仍然响应
        self.status_label.setText(f"UI响应正常 - {time.strftime('%H:%M:%S')}")
    
    def closeEvent(self, event):
        # 关闭窗口时停止线程
        self.stop_task()
        event.accept()


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = ThreadingDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()