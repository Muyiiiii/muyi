# muyi

Some useful utils for GNNs and Deep Learning.

## Installation

```bash
pip install muyi              # basic installation
pip install muyi[plot]        # + matplotlib
pip install muyi[csv]         # + pandas, tqdm
pip install muyi[gpu]         # + GPUtil
pip install muyi[graph]       # + torch, dgl
pip install muyi[all]         # all dependencies
```

## utils

1. `color_print(content, font_color, bg_color)`
2. `save_pic_iterly(pic_name, postfix, info)`
3. `read_csv_tqdm(path, **kwargs)`
4. `save_result_csv(csv_path, data)`
5. `get_unique_save_path(folder_path, base_name_pattern, start_no)`

## graph

1. `pyg_data_to_dgl_graph(pyg_data_obj)`

## gpu

1. `get_gpu_memory_usage()`
2. `display_gpu_memory_usage()`

## Upload to PyPI

```bash
# 1. Install build tools
pip install build twine

# 2. Build package
python -m build

# 3. Upload to PyPI
twine upload dist/*
# Username: __token__
# Password: your PyPI API Token (starts with pypi-)
```

Get API Token: https://pypi.org/manage/account/token/

### Save Token Locally (Optional)

Create `~/.pypirc` file to avoid entering credentials each time:

```ini
[pypi]
username = __token__
password = pypi-your-token-here
```

- **Linux/macOS**: `~/.pypirc`
- **Windows**: `C:\Users\<username>\.pypirc`
