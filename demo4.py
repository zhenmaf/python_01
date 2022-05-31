

# alst = []
blst = [11,23,'hds',None]

# print(alst)
# print(blst)

# for x in blst:
#     print("列表中的值:",x)


#列表的方法:
clst = ['red','green','blue']

# 列表中添加元素：list.append
clst.append('black')
print("使用append添加元素后的列表:",clst)

# 向列表中追加一个其他列表内的元素：list.extend
clst.extend(blst)
print("追加blst后的结果:",clst)

# 列表翻转：list。recerse
clst.reverse()
print("翻转后的结果:",clst)

# 列表排序：list.sort(),里面的元素必须是同类型的
# clst.sort()
# print("排序后的结果:",clst)

# 通级在列表中出现的次数：list.count(obj)
print(clst.count('blue'))

# 从列表中找到某个元素的位置：list.index(obj)
print(clst.index('black'))

# 向列表中的某个位置插入元素：list.insert(index,obj)
clst.insert(1,'hello')
print(clst)

# 打印1-10所有的数
for x in [1,2,3,4,5,6,7,8,9,10]:
    print('列表的数',x)