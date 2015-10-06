# -*- coding: utf-8 -*-
"""
Created on Thu Sep 03 10:42:12 2015

@author: erica
"""
from factual import Factual
prmpt = '> '
# getting paramaters 
print 'Enter Key:' 
key = raw_input(prmpt)
print 'Enter Secret:'
scrt = raw_input(prmpt)
factual = Factual(key, scrt)
places = factual.table('places')
data = places.filters({'$and':[{'category_ids':{'$includes':9}},{'locality':{'$eq':'chicago'}}]}).data()
print(data)
