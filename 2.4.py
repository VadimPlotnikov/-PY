import subprocess
import os
os.makedirs('Result')

from os import listdir

list_files = (listdir ('./Sourdce/'))

for ff in list_files:
    rr = './Sourdce/'+ff #создание пути к исходному файлу
    tt = './Result/'+ff #путь для результата
    jj = 'convert.exe '+ rr+ ' -resize 200 '+tt # создание аргумента для subprocess.run
    nn = subprocess.run(jj)




