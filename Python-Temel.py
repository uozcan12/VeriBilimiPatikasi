# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:

# input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

#output: [1,'a','cat',2,3,'dog',4,5]

from collections.abc import Iterable

def flatten(l):
  for el in l:
    if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
      yield from flatten(el)
    else:
      yield el

l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
mygenerator = flatten(l) # create a generator
returned_list = [ i for i in mygenerator]
print(returned_list)
  

#2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:

#input: [[1, 2], [3, 4], [5, 6, 7]]

#output: [[[7, 6, 5], [4, 3], [2, 1]]


def reverse_variables(input_list):  
  for i in range(len(input_list)):
    input_list[i] = input_list[i][::-1]
  return input_list[::-1]  

l = [[1, 2], [3, 4], [5, 6, 7]]
reverse_variables(l)
