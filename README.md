# docts

python package docts

## install

```sh
pip install -U docts
pip install git+ssh://git@github.com/foyoux/docts.git
pip install git+https://github.com/foyoux/docts.git
```

## 翻译 xlf 文件

> 将文档提取到 xlf 文件 或 将 xlf 文件重新生成文档，请参阅 [旧文档 - 仅作参考](https://github.com/foyoux/docts/wiki/%E6%97%A7%E6%96%87%E6%A1%A3)
> 
> 代码看下面

```py
from pygtrans import Translate

from docts import Docts

if __name__ == '__main__':
    translator = Translate(proxies={'https': 'http://localhost:10809'})
    doc = Docts('<xlf_file_path>', translator)
    # 翻译完成的将保存到 xlf_file_path 文件同目录
    doc.save_words()
```