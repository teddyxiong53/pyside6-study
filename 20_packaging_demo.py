#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 20：应用程序打包与部署（简化版）
目标：展示PyInstaller打包的关键概念
学习点：资源文件处理、打包配置、单文件/目录结构打包

这是一个简化版的示例，不依赖PySide6，可以直接运行。
完整版请参考 20_packaging.py（需要安装PySide6）
"""

import sys
import os
import tkinter as tk
from tkinter import messagebox, filedialog


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


class PackagingDemo:
    def __init__(self, root):
        self.root = root
        
        # 设置窗口标题和大小
        root.title("应用程序打包示例（简化版）")
        root.geometry("600x400")
        
        # 创建标题
        title_label = tk.Label(root, text="PyInstaller 应用程序打包与部署", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)
        
        # 添加说明
        description = tk.Label(
            root, 
            text="这是一个演示如何使用PyInstaller打包应用的示例。\n打包后的应用可以在没有Python环境的计算机上运行。",
            wraplength=500
        )
        description.pack(pady=10)
        
        # 资源文件演示
        resource_label = tk.Label(root, text="资源文件演示：", font=("Arial", 12, "bold"))
        resource_label.pack(pady=5)
        
        # 资源路径显示
        self.resource_path_label = tk.Label(
            root, 
            text=f"资源文件路径: {resource_path('resources/example.svg')}",
            wraplength=500,
            relief=tk.GROOVE,
            padx=10,
            pady=10
        )
        self.resource_path_label.pack(pady=10)
        
        # 添加按钮
        load_button = tk.Button(root, text="加载资源文件信息", command=self.load_resource_info)
        load_button.pack(pady=5)
        
        file_button = tk.Button(root, text="选择文件", command=self.select_file)
        file_button.pack(pady=5)
        
        info_button = tk.Button(root, text="查看打包说明", command=self.show_packaging_info)
        info_button.pack(pady=5)
    
    def load_resource_info(self):
        """显示资源文件信息"""
        resource_file = resource_path("resources/example.svg")
        file_exists = os.path.exists(resource_file)
        
        if file_exists:
            file_size = os.path.getsize(resource_file)
            info = f"资源文件: {resource_file}\n文件大小: {file_size} 字节\n状态: 文件存在"
        else:
            info = f"资源文件: {resource_file}\n状态: 文件不存在"
        
        self.resource_path_label.config(text=info)
    
    def select_file(self):
        """文件选择对话框示例"""
        file_path = filedialog.askopenfilename(
            title="选择文件",
            filetypes=[("所有文件", "*.*"), ("图片文件", "*.png *.jpg *.svg")]
        )
        
        if file_path:
            messagebox.showinfo("文件已选择", f"已选择文件: {file_path}")
    
    def show_packaging_info(self):
        """显示打包说明信息"""
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
        
        info_window = tk.Toplevel(self.root)
        info_window.title("PyInstaller 打包说明")
        info_window.geometry("600x400")
        
        text_widget = tk.Text(info_window, wrap=tk.WORD, padx=10, pady=10)
        text_widget.insert(tk.END, packaging_info)
        text_widget.config(state=tk.DISABLED)
        text_widget.pack(fill=tk.BOTH, expand=True)
        
        close_button = tk.Button(info_window, text="关闭", command=info_window.destroy)
        close_button.pack(pady=10)


def main():
    # 创建主窗口
    root = tk.Tk()
    app = PackagingDemo(root)
    
    # 进入事件循环
    root.mainloop()


if __name__ == "__main__":
    main()