# -*- coding: utf-8 -*-
"""testmodkh.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14ugYLtcZ3Z7IOe4ymhsagqeIReKti7Av
"""

def square(nb):
  return nb**2

def cube(nb):
  return nb**3

def absolute(nb):
  if nb < 0: 
   return nb*-1
  else:
   return nb

def factor(nb):
  res = 1
  for i in range(1,nb+1):
    res = i*res
  return res

list13 =  [10,20,30]

def moy(dataset):
  total = 0
  for i in dataset:
    total = total + i
  return total/len(dataset)

def minimum(liste):
    valeur_min = liste[0]
    for i in liste :
        if i <= valeur_min:
            valeur_min = i
    return valeur_min

def maximum(liste):
    valeur_max = liste[0]
    for i in liste :
        if i >= valeur_max:
            valeur_max = i
    return valeur_max