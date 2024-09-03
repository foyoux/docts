# docts

`docts` 是一个利用 pygtrans 库翻译和处理 XLF 文件的 Python 包。

## 功能简介

- **XLF 文件解析**：提取 XLF 文件中的源文本。
- **文本过滤**：通过自定义过滤器，排除不需要翻译的内容。
- **文本映射**：替换特定符号或字符串。
- **批量翻译**：利用 Google 翻译 API 进行批量翻译。
- **XLF 文件写入**：将翻译结果写回新的 XLF 文件。

## 安装

你可以通过以下几种方式安装 `docts`：

```sh
pip install -U docts
pip install git+ssh://git@github.com/foyoux/docts.git
pip install git+https://github.com/foyoux/docts.git
```

## 使用方法

### 基本使用

`docts` 主要用于将 XLF 文件中的内容提取、翻译并重新保存。以下是一个基本的使用示例：

```python
from pygtrans import Translate
from docts import Docts

if __name__ == '__main__':
    # 创建翻译客户端，指定代理（如有需要）
    translator = Translate(proxies={'https': 'http://localhost:10809'})
    
    # 初始化 Docts 实例，指定 XLF 文件路径和翻译客户端
    doc = Docts('<xlf_file_path>', translator)
    
    # 过滤无效或不需要翻译的文本（可选）
    doc.add_filter(lambda word: 'filter_condition' in word)
    
    # 执行翻译并保存结果，翻译后的 XLF 文件将保存在同一目录下
    translated_file_path = doc.save_words()
    print(f"翻译完成，结果保存至: {translated_file_path}")
```

### 进阶使用

#### 自定义过滤器

你可以通过添加不同的过滤器来定制处理流程。例如，过滤掉所有包含等号（`=`）的行：

```python
doc.add_filter(lambda word: '=' in word)
```

#### 使用正则表达式过滤

支持通过正则表达式过滤文本。例如，过滤所有以 `error` 开头的字符串：

```python
import re

doc.add_contain_filter(re.compile(r'^error'))
```

#### 自定义文本映射

将特定符号映射为其他符号，例如将 `•` 替换为 `●`：

```python
doc.add_map(lambda word: word.replace('•', '●'))
```

#### 重置过滤

如果想要撤销之前的过滤操作，可以使用 `reset()` 方法恢复原始文本列表：

```python
doc.reset()
```

#### 保存忽略的文本

除了保存翻译结果外，你还可以将被过滤掉的文本单独保存：

```python
ignored_file_path = doc.save_ignores()
print(f"忽略的文本已保存至: {ignored_file_path}")
```

## 具体流程

请参阅 [旧文档](https://github.com/foyoux/docts/wiki/%E6%97%A7%E6%96%87%E6%A1%A3) （仅作参考）。
