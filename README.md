# bwav-otio-composer

一个用于将音频文件转换为 OpenTimelineIO (OTIO) 时间轴文件的 Python 工具。

## 功能特性

- 🎵 自动扫描音频文件目录
- 🎬 生成符合 DaVinci Resolve 标准的 OTIO 时间轴
- 🎭 支持角色分组和轨道管理
- ⚡ 高效的音频剪辑合成算法
- 🛠️ 命令行界面，易于使用

## 快速开始

### 1. 安装

```bash
# 克隆项目
git clone <repository-url>
cd bwav_otio_composer

# 安装包
pip install -e .
```

### 2. 使用

```bash
# 查看帮助
bwav-otio-composer --help

# 基本使用（使用默认参数）
bwav-otio-composer

# 指定音频文件路径
bwav-otio-composer --path /path/to/audio/files

# 指定输出文件名和帧率
bwav-otio-composer --path audio_files --output my_project --fps 25.0
```

### 3. 快速启动

运行快速启动脚本来自动设置环境：

```bash
python quick_start.py
```

## 参数说明

| 参数 | 短参数 | 说明 | 默认值 |
|------|--------|------|--------|
| `--path` | `-p` | 音频文件目录路径 | `test_data` |
| `--output` | `-o` | 输出文件名 | 自动生成 |
| `--fps` | `-f` | 帧率 | `24.0` |

## 项目结构

```
bwav_otio_composer/
├── src/bwav_otio_composer/
│   ├── __init__.py              # 主入口点
│   ├── otio_generator.py        # OTIO生成器主模块
│   ├── audio_composer/          # 音频合成模块
│   │   ├── composer/            # 合成算法
│   │   │   ├── audio_to_timeline.py
│   │   │   ├── scanline_composer.py
│   │   │   └── greedy_heapsort_composer.py
│   │   └── models/              # 数据模型
│   │       ├── audioclip.py
│   │       └── audiotrack.py
│   └── utils/                   # 工具模块
│       └── logger.py
├── pyproject.toml               # 项目配置
├── INSTALLATION.md              # 详细安装指南
├── test_install.py              # 安装测试脚本
├── example_usage.py             # 使用示例
└── quick_start.py               # 快速启动脚本
```

## 依赖项

- Python >= 3.12
- click >= 8.1.8
- opentimelineio >= 0.17.0
- pydantic >= 2.10.4
- pytest >= 8.3.4
- wavinfo >= 3.1.0

## 开发

### 安装开发依赖

```bash
pip install -e .
```

### 运行测试

```bash
python test_install.py
```

### 修改代码后重新安装

```bash
pip install -e . --force-reinstall
```

## 故障排除

### 常见问题

1. **导入错误**
   - 确保已正确安装包：`pip install -e .`
   - 检查 Python 版本是否 >= 3.12

2. **模块找不到**
   - 检查项目结构是否正确
   - 确保所有 `__init__.py` 文件存在

3. **权限问题**
   - Windows 用户可能需要以管理员身份运行命令提示符

### 获取帮助

如果遇到问题，请：

1. 运行 `python test_install.py` 检查安装状态
2. 查看 `INSTALLATION.md` 获取详细安装指南
3. 运行 `bwav-otio-composer --help` 查看命令行帮助

## 许可证

[添加许可证信息]

## 贡献

欢迎提交 Issue 和 Pull Request！

## 更新日志

### v0.1.0
- 初始版本
- 支持基本的音频到 OTIO 转换功能
- 实现角色分组和轨道管理
