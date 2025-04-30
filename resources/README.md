# PySide6 应用打包资源

本文件夹包含用于PySide6应用打包示例的资源文件。

## 文件说明

- `example.svg` - 示例图像，用于演示如何在打包应用中加载和显示资源文件
- `app_icon.svg` - 应用图标，用于设置窗口图标和创建可执行文件图标

## 打包说明

在使用PyInstaller打包应用时，需要确保这些资源文件被正确包含在打包后的应用中。

### 包含资源文件的命令示例

```bash
# Windows系统
pyinstaller --name="MyApp" --windowed --icon=resources/app_icon.svg --add-data="resources;resources" 20_packaging.py

# macOS/Linux系统
pyinstaller --name="MyApp" --windowed --icon=resources/app_icon.svg --add-data="resources:resources" 20_packaging.py
```

### 在代码中访问资源文件

打包后的应用中，可以使用`resource_path`函数获取资源文件的路径：

```python
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# 使用示例
icon_path = resource_path("resources/app_icon.svg")
```

## 注意事项

- 在不同操作系统上，`--add-data`参数的分隔符不同：
  - Windows使用分号 (`;`)
  - macOS/Linux使用冒号 (`:`)
- 对于图标文件，Windows系统通常需要`.ico`格式，可以使用在线工具将SVG转换为ICO格式
- 在macOS上，可能需要额外的步骤来创建完整的应用包