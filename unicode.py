#!/usr/bin/env python3

def encode(s, encoding):
    coded = s.encode(encoding)
    print('=>', encoding )
    print(type(coded), coded.hex())
    print()


s = '你好世界！'
print(type(s), s)
print([hex(ord(c)) for c in s])
print()

encode(s, 'utf-8')
encode(s, 'utf-16')
encode(s, 'utf-16le')
encode(s, 'utf-16be')
encode(s, 'utf-32')
