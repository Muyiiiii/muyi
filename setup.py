import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="Muyi",  # 模块名称
    version="0.0.9",  # 当前版本
    author="muyiiiii",  # 作者
    author_email="",  # 作者邮箱
    description="Some useful utils.",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    url="https://github.com/Muyiiiii/muyi",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        # 无核心依赖，所有依赖都是可选的
    ],
    # 可选依赖
    extras_require={
        'plot': ['matplotlib'],           # save_pic_iterly
        'csv': ['pandas', 'tqdm'],        # read_csv_tqdm
        'gpu': ['GPUtil'],                # get_gpu_memory_usage
        'graph': ['torch', 'dgl'],        # pyg_data_to_dgl_graph
        'all': [                          # 安装全部
            'matplotlib',
            'pandas',
            'tqdm',
            'GPUtil',
            'torch',
            'dgl',
        ],
    },
    python_requires='>=3',
)