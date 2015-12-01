# -*- coding: utf-8 -*-
"""
Created on Tue Dec 01 19:33:55 2015

@author: FRDB
"""

import urllib2
pagina = urllib2.urlopen('http://www.horariodebrasilia.org/')
conteudo = pagina.readlines()
print(str(conteudo[56])[33:68].replace('Ã§', 'ç')+' '+str(conteudo[57])[31:39])