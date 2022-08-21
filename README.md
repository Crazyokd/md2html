使用 [mistune](https://github.com/lepture/mistune) 和 [github-markdown-css](https://github.com/sindresorhus/github-markdown-css) 解析并渲染 `md` 文件。

![snapshot](https://cdn.sxrekord.com/blog/md2html_example.jpg)
## Features
- 一个命令完成任务
- 解析得到的 html 页面内嵌源文件
- 可通过修改[custom.css](css/custom.css)和[custom.js](js/custom.js)自定义页面效果

## Usage
```shell
# 运行脚本
source convert.sh

# 清理目录
source clean.sh
```

## Acknowledge
- use [mistune](https://github.com/lepture/mistune) to parse MD format to HTML format.
- use [github-markdown-css](https://github.com/sindresorhus/github-markdown-css) to render html pages.

## TODO
- [ ] 模式切换时背景图片平滑过渡
- [ ] 脚本更新[github-markdown-css](https://github.com/sindresorhus/github-markdown-css)