# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하세요

import fnmatch

list = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in list:
    if fnmatch.fnmatch(file, '*.h'):
        print(file)