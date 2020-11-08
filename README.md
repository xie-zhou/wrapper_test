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
```
随后打开当中的setup.py 修改第25行:
```python
25|conf = config.ConfigParser()
25|conf = config.RawConfigParser()
```
然后安装:
```bash
python setup.py install
```

安装后需要修改源文件中的一个bug
    /your_env/astromatic_wrapper/utils/pipeline.py中
```python
77|     from astropy.extern.six import string_types
77|     from six import string_types
```
