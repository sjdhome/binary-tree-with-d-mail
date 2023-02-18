#!/usr/bin/env python3
# 导入随机模块
import random

# 定义节点类
class Node:
    # 初始化节点，给定值和子节点
    def __init__(self, value, child=None):
        self.value = value
        self.child = child
    
    # 生成新节点的方法，返回新节点
    def generate(self):
        # 生成新节点的值，0或1的概率各50%
        new_value = random.randint(0, 1)
        # 创建新节点
        new_node = Node(new_value)
        # 将新节点作为子节点
        self.child = new_node
        # 返回新节点
        return new_node
    
    # 改变节点值的方法，无返回值
    def change(self):
        # 改变节点值，0变1，1变0
        self.value = 1 - self.value
        # 销毁子节点
        self.child = None
    
    # 用字符串表示节点的方法，返回字符串
    def __str__(self):
        # 用括号表示节点，用逗号分隔子节点
        s = str(self.value)
        if self.child:
            s += "," + str(self.child)
        return s

# 创建根节点，值为0
root = Node(0)
# 打印根节点
print(root)
# 模拟生成新节点
for i in range(1000):
    # 随机选择一个节点
    node = root
    while node.child:
        node = node.child
    # 生成新节点的概率是50%
    if random.random() < 0.5:
        node = node.generate()
    # 改变节点值的概率是10%
    if random.random() < 0.1:
        # 随机选择一个之前生成的子节点
        node = root
        while node.child and random.random() < 0.5:
            node = node.child
        # 改变该节点的值
        node.change()
    # 打印根节点
    print(root)
