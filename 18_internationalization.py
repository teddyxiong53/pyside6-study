#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 18：国际化（多语言支持）
目标：实现中英文切换
学习点：多语言文件生成与加载
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox
from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo


class I18nDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("国际化示例")
        self.resize(400, 300)
        
        # 创建翻译器
        self.translator = QTranslator()
        
        # 创建UI
        self.init_ui()
    
    def init_ui(self):
        # 创建主布局
        layout = QVBoxLayout()
        
        # 创建语言选择下拉框
        self.lang_combo = QComboBox()
        self.lang_combo.addItem("中文", "zh_CN")
        self.lang_combo.addItem("English", "en_US")
        self.lang_combo.currentIndexChanged.connect(self.change_language)
        layout.addWidget(QLabel("选择语言/Select Language:"))
        layout.addWidget(self.lang_combo)
        
        # 添加一些示例文本和按钮
        self.welcome_label = QLabel("欢迎使用PySide6国际化示例")
        layout.addWidget(self.welcome_label)
        
        self.intro_label = QLabel("这是一个演示如何实现多语言支持的示例程序")
        layout.addWidget(self.intro_label)
        
        self.ok_button = QPushButton("确定")
        layout.addWidget(self.ok_button)
        
        self.cancel_button = QPushButton("取消")
        layout.addWidget(self.cancel_button)
        
        # 设置窗口布局
        self.setLayout(layout)
        
        # 注意：在实际应用中，你需要使用Qt的tr()函数标记需要翻译的字符串
        # 并使用Qt Linguist工具生成翻译文件(.ts)和编译后的翻译文件(.qm)
        # 这里我们只是模拟翻译效果
    
    def change_language(self, index):
        # 获取选择的语言代码
        lang_code = self.lang_combo.itemData(index)
        
        # 在实际应用中，你会加载真正的翻译文件
        # self.translator.load(f"{lang_code}.qm")
        # QApplication.instance().installTranslator(self.translator)
        
        # 这里我们只是模拟翻译效果
        if lang_code == "en_US":
            self.setWindowTitle("Internationalization Example")
            self.welcome_label.setText("Welcome to PySide6 Internationalization Example")
            self.intro_label.setText("This is a demo showing how to implement multi-language support")
            self.ok_button.setText("OK")
            self.cancel_button.setText("Cancel")
        else:
            self.setWindowTitle("国际化示例")
            self.welcome_label.setText("欢迎使用PySide6国际化示例")
            self.intro_label.setText("这是一个演示如何实现多语言支持的示例程序")
            self.ok_button.setText("确定")
            self.cancel_button.setText("取消")


# 以下是实际应用中如何生成和使用翻译文件的步骤注释：
"""
1. 使用Qt Linguist工具链生成翻译文件：
   - 使用pylupdate6工具从Python源代码中提取需要翻译的字符串到.ts文件
     pylupdate6 your_app.py -ts translations/en_US.ts translations/zh_CN.ts
   
   - 使用Qt Linguist编辑.ts文件，添加翻译
   
   - 使用lrelease工具将.ts文件编译为.qm文件
     lrelease translations/en_US.ts translations/zh_CN.ts

2. 在应用程序中加载翻译文件：
   translator = QTranslator()
   if translator.load("translations/" + locale + ".qm"):
       app.installTranslator(translator)

3. 使用tr()函数标记需要翻译的字符串：
   self.label.setText(self.tr("Hello World"))
"""


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = I18nDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()