
#append
"""x = [1,2,3]
y = [4,5,6]
x.append(y)
print(x)"""


#extend
'''x = [1,2,3]
y = [4,5,6]
x.extend(y)
print(x)'''


#insert
'''x=[1,2,3]
x.insert(2,"aaa")
print(x)'''


#del
'''x=[1,2,3,4]
del x[0]
print(x)
del x[:3]
print(x)
'''


#remove(找到第一個和指定內容相同)
'''x=[1,2,3,4,5,3]
x.remove(3)
print(x)
x.remove(3)
print(x)'''


#sorted
'''x=[4,2,3,1]
y=sorted(x)
print(y)
z=sorted(x,reverse=True)
print(z)'''

#else list操作
'''print(3 in [1,2,3])
print(3 not in [1,2,3])
z=[1,3] * 2
print(z)
a = min([1,2,3,4,6,8])
b = max([1,2,1,4,5,6])
print(a)
print(b)
#index找3的位置
x = [1,2,3,3,3,3,4,5,6]
print(x.index(3))
print(x.count(3))'''
