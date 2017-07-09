#!/usr/bin/env python3
#coding:utf-8

import xml.etree.ElementTree as ET


tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)

# 遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag, i.text)

# 只遍历year 节点
for node2 in root.iter('year'):
    print(node2.tag, node2.text)

for node1 in root.iter('country'):
    print(node1.tag, node1.attrib)