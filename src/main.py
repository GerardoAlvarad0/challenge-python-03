# -*- config: utf-8 -*-

import re


def run():
    with open('encoded.txt', 'r', encoding='utf-8') as f:
        code = f.read()
    
    pattern = re.compile(r'[a-z]')
    decode = ''.join(pattern.findall(code))
    print("El mensaje secreto es: ",decode)

if __name__ == '__main__':
    run()
