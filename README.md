# 测试wrapper

## 安装SExtractor

官网的安装太复杂了

```bash
conda install -c conda-forge astromatic-source-extractor
```

## 安装SCAMP

官网的安装太复杂了

```bash
conda install -c conda-forge astromatic-scamp
```

## 安装astromatic_wrapper

```bash
git clone https://github.com/fred3m/astromatic_wrapper.git
cd astromatic_wrapper
python setup.py install
```

安装后需要修改源文件中的一个bug
    /your_env/astromatic_wrapper/utils/pipeline.py中
```python
77|     from astropy.extern.six import string_types
77|     from six import string_types
```
