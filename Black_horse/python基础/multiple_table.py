#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
for x in range(1,10):
    for y in range (1,x+1):
        #print('%s*%s=%s'%(x,y,x*y),end='   ')
        sys.stdout.write('%s*%s=%s\t'%(x,y,x*y))
        if y == x :
            print('\t')
'''
#!/bin/bash
#

echo 'this is a mutiple_table'
for ((i=1;i<=9;i++))
do 
  for ((j=1;j<=i;j++))
  do 
  echo "$i*$j=$((i*j))\t"
  done
  echo
done
'''