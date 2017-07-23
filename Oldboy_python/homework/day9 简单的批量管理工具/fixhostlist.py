#!/usr/bin/env python3
#coding:utf-8

import pickle

hostlist1 = {'192.168.1.141':('root','8520'),'192.168.1.139':('root','8520')}

hostlist2 = {'59.110.231.224':('root','hq1187984211.')}

with open('hostgroup/group1','wb') as f :
    pickle.dump(hostlist1,f)

with open('hostgroup/group2','wb') as f :
    pickle.dump(hostlist2,f)

