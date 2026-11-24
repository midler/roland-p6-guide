import re,sys
src=open(sys.argv[1],encoding='utf-8').read()
i=src.index('<header')
head,body=src[:i],src[i:]
html='''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Интерактивный курс по сэмплеру Roland P-6: уроки с точными нажатиями, сетки битов, аккорды, жанровые рецепты.">
<style>html{-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
'''+head.strip()+'''
</head>
<body>
'''+body.strip()+'''
</body>
</html>
'''
open(sys.argv[2],'w',encoding='utf-8').write(html)
