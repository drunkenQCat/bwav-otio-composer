#!/usr/bin/env python3
"""
bwav-otio-composer 使用示例

这个脚本展示了如何使用 bwav-otio-composer 包来生成 OTIO 时间轴文件。
"""

import sys
import os

# 添加项目根目录到 Python 路径
import bwav_otio_composer

def example_usage():
    """使用示例"""
    try:
        from bwav_otio_composer.otio_generator import generate_otio
        
        print("🎵 bwav-otio-composer 使用示例")
        print("=" * 50)
        
        # 示例1：使用默认参数
        print("\n1. 使用默认参数生成 OTIO 文件：")
        print("   generate_otio()")
        
        # 示例2：指定参数
        print("\n2. 指定参数生成 OTIO 文件：")
        print("   generate_otio(path='audio_files', output='my_project', fps=25.0)")
        
        # 示例3：命令行使用
        print("\n3. 命令行使用：")
        print("   bwav-otio-composer --path audio_files --output my_project --fps 25.0")
        
        print("\n✅ 包配置正确，可以正常使用！")
        
    except ImportError as e:
        print(f"❌ 导入失败：{e}")
        print("\n请先安装包：")
        print("pip install -e .")

if __name__ == "__main__":
    example_usage() 