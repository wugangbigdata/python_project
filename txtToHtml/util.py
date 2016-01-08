#coding=utf-8
#文本块生成器
#将文本切分成一个一个段落（块）

def lines(file):
    for line in file:
        yield  line
    yield '\n'  #在文件最后追加一个空行

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():       #以空行分割块
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []

