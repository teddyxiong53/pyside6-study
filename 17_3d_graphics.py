#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demo 17：3D图形（Qt3D）
目标：基础3D渲染
学习点：Qt3D模块使用
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSlider, QLabel
from PySide6.QtCore import Qt
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.Qt3DRender import Qt3DRender


class ThreeDDemo(QWidget):
    def __init__(self):
        super().__init__()
        
        # 设置窗口标题和大小
        self.setWindowTitle("3D图形示例")
        self.resize(800, 600)
        
        # 创建UI
        self.init_ui()
    
    def init_ui(self):
        # 创建主布局
        main_layout = QVBoxLayout()
        
        # 创建3D窗口
        self.view = Qt3DExtras.Qt3DWindow()
        self.view.defaultFrameGraph().setClearColor(Qt.white)
        
        # 创建容器窗口部件
        container = QWidget.createWindowContainer(self.view)
        container.setMinimumSize(200, 100)
        container.setFocusPolicy(Qt.NoFocus)
        
        # 添加3D窗口到布局
        main_layout.addWidget(container)
        
        # 创建控制面板
        control_layout = QHBoxLayout()
        
        # 添加旋转滑块
        control_layout.addWidget(QLabel("旋转:"))
        self.rotation_slider = QSlider(Qt.Horizontal)
        self.rotation_slider.setRange(0, 360)
        self.rotation_slider.setValue(0)
        self.rotation_slider.valueChanged.connect(self.update_rotation)
        control_layout.addWidget(self.rotation_slider)
        
        # 添加缩放滑块
        control_layout.addWidget(QLabel("缩放:"))
        self.scale_slider = QSlider(Qt.Horizontal)
        self.scale_slider.setRange(1, 100)
        self.scale_slider.setValue(50)
        self.scale_slider.valueChanged.connect(self.update_scale)
        control_layout.addWidget(self.scale_slider)
        
        # 添加控制面板到主布局
        main_layout.addLayout(control_layout)
        
        # 设置窗口布局
        self.setLayout(main_layout)
        
        # 初始化3D场景
        self.init_scene()
    
    def init_scene(self):
        # 创建根实体
        self.root_entity = Qt3DCore.QEntity()
        
        # 创建相机
        self.camera = self.view.camera()
        self.camera.setPosition(Qt3DCore.QVector3D(0, 0, 20.0))
        self.camera.setViewCenter(Qt3DCore.QVector3D(0, 0, 0))
        
        # 创建相机控制器
        camera_controller = Qt3DExtras.QOrbitCameraController(self.root_entity)
        camera_controller.setCamera(self.camera)
        
        # 创建立方体实体
        self.cube_entity = Qt3DCore.QEntity(self.root_entity)
        
        # 创建立方体网格
        cube_mesh = Qt3DExtras.QCuboidMesh()
        
        # 创建材质
        material = Qt3DExtras.QPhongMaterial(self.root_entity)
        material.setDiffuse(Qt.blue)
        
        # 创建变换组件
        self.transform = Qt3DCore.QTransform()
        self.transform.setScale(1.0)
        self.transform.setRotation(Qt3DCore.QQuaternion.fromAxisAndAngle(Qt3DCore.QVector3D(1, 0, 0), 0))
        
        # 将组件添加到实体
        self.cube_entity.addComponent(cube_mesh)
        self.cube_entity.addComponent(material)
        self.cube_entity.addComponent(self.transform)
        
        # 设置根实体
        self.view.setRootEntity(self.root_entity)
    
    def update_rotation(self, value):
        # 更新旋转角度
        self.transform.setRotation(Qt3DCore.QQuaternion.fromAxisAndAngle(Qt3DCore.QVector3D(0, 1, 0), value))
    
    def update_scale(self, value):
        # 更新缩放比例
        scale = value / 50.0
        self.transform.setScale(scale)


def main():
    # 创建应用程序对象
    app = QApplication(sys.argv)
    
    # 创建窗口
    window = ThreeDDemo()
    
    # 显示窗口
    window.show()
    
    # 进入事件循环
    sys.exit(app.exec())


if __name__ == "__main__":
    main()