#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 20：应用程序打包与部署
目标：使用PyInstaller将PySide6应用打包成可执行文件
学习点：资源文件处理、图标设置、单文件/目录结构打包

注意：运行此示例前，请确保已安装PySide6：
pip install PySide6

打包命令示例：
1. 基本打包：
   pyinstaller --name="MyApp" --windowed main.py

2. 单文件打包：
   pyinstaller --name="MyApp" --windowed --onefile main.py

3. 添加图标：
   pyinstaller --name="MyApp" --windowed --icon=app_icon.ico main.py

4. 包含数据文件：
   pyinstaller --name="MyApp" --windowed --add-data="resources:resources" main.py

5. 完整打包示例：
   pyinstaller --name="MyApp" --windowed --onefile --icon=app_icon.ico --add-data="resources:resources" main.py

注意事项：
1. 在macOS上，--windowed选项会创建.app包
2. 在Windows上，--windowed选项会创建无控制台窗口的应用
3. 资源文件路径格式在不同操作系统上有所不同：
   - Windows: --add-data="resources;resources"
   - macOS/Linux: --add-data="resources:resources"
"""

import sys
import os
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QPushButton, QFileDialog, QMessageBox)
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtCore import Qt


# 获取资源文件的绝对路径
def resource_path(relative_path):
    """
    获取资源的绝对路径，兼容开发环境和PyInstaller打包后的环境
    
    在开发环境中，直接返回相对路径
    在打包环境中，返回临时文件夹中的资源路径
    """
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        # 开发环境下，使用当前目录
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)


class PackagingDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("应用程序打包示例")
        self.resize(600, 400)
        
        # 设置窗口图标
        self.setWindowIcon(QIcon(resource_path("resources/app_icon.svg")))
        
        # 创建中央部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 添加标题
        title = QLabel("PySide6 应用程序打包与部署")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Bold))
        layout.addWidget(title)
        
        # 添加说明
        description = QLabel(
            "这是一个演示如何使用PyInstaller打包PySide6应用的示例。\n"
            "打包后的应用可以在没有Python环境的计算机上运行。"
        )
        description.setAlignment(Qt.AlignCenter)
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # 添加资源文件演示
        resource_label = QLabel("资源文件演示：")
        resource_label.setFont(QFont("Arial", 12, QFont.Bold))
        layout.addWidget(resource_label)
        
        # 添加按钮
        self.load_image_btn = QPushButton("加载图片资源")
        self.load_image_btn.clicked.connect(self.load_image)
        layout.addWidget(self.load_image_btn)
        
        # 图片显示区域
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setMinimumHeight(200)
        layout.addWidget(self.image_label)
        
        # 添加文件选择按钮
        self.select_file_btn = QPushButton("选择文件")
        self.select_file_btn.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_btn)
        
        # 添加打包说明按钮
        self.packaging_info_btn = QPushButton("查看打包说明")
        self.packaging_info_btn.clicked.connect(self.show_packaging_info)
        layout.addWidget(self.packaging_info_btn)
    
    def load_image(self):
        """
        加载资源图片示例
        注意：在实际应用中，你需要准备资源文件并放在resources文件夹中
        """
        try:
            # 加载SVG资源图片
            pixmap = QPixmap(resource_path("resources/example.svg"))
            self.image_label.setPixmap(pixmap.scaled(300, 200, Qt.KeepAspectRatio))
            
            # 显示资源路径信息
            self.image_label.setToolTip("资源文件路径：" + 
                                  resource_path("resources/example.svg"))
            self.image_label.setStyleSheet("border: 1px solid #ccc; padding: 10px;")
        except Exception as e:
            QMessageBox.warning(self, "资源加载错误", f"无法加载资源文件: {str(e)}")
    
    def select_file(self):
        """
        文件选择对话框示例
        """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择文件", "", "所有文件 (*);;图片文件 (*.png *.jpg)"
        )
        
        if file_path:
            QMessageBox.information(self, "文件已选择", f"已选择文件: {file_path}")
    
    def show_packaging_info(self):
        """
        显示打包说明信息
        """
        packaging_info = """
        PyInstaller 打包步骤：
        
        1. 安装 PyInstaller：
           pip install pyinstaller
        
        2. 基本打包命令：
           pyinstaller --name="MyApp" --windowed main.py
        
        3. 单文件打包：
           pyinstaller --name="MyApp" --windowed --onefile main.py
        
        4. 添加图标：
           pyinstaller --name="MyApp" --windowed --icon=app_icon.ico main.py
        
        5. 包含数据文件：
           Windows: pyinstaller --name="MyApp" --add-data="resources;resources" main.py
           macOS/Linux: pyinstaller --name="MyApp" --add-data="resources:resources" main.py
        
        6. 创建规范文件后修改：
           pyinstaller --name="MyApp" main.py
           # 编辑生成的 MyApp.spec 文件，然后运行：
           pyinstaller MyApp.spec
        
        注意事项：
        - 确保所有资源文件都被正确包含
        - 测试打包后的应用在目标环境中是否正常运行
        - 对于复杂应用，建议使用 .spec 文件进行配置
        """
        
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("PyInstaller 打包说明")
        msg_box.setText(packaging_info)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = PackagingDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()