#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import re

re.search(r'\d+', 'cost:9000')
# Out[3]:
# <_sre.SRE_Match object; span=(5, 9), match='9000'>

re.search(r'\d+', 'cost:9000')
# Out[5]:
# <_sre.SRE_Match object; span=(5, 9), match='9000'>

re.search(r'\d+', 'cost:9000,200')
# Out[6]:
# <_sre.SRE_Match object; span=(5, 9), match='9000'>

re.findall(r'\d+', 'cost:9000,200')
# Out[7]:
# ['9000', '200']


re.sub(r'\d+', '200', 'cost : 500,python :300')
# Out[9]:
'cost : 200,python :200'
