import os
#这个只是生成list 不会显示list
list1 = [x*x for x in range(1,11)]
print(list1)

#加入if判断
list2 = [x*x for x in range(1,11) if x%2 ==0 ]
print(list2)

#两层循环，甚至更多循环
list_double_for = [m+n for m in 'ABC' for n in 'XYZ']
print(list_double_for)

#列出指定目录下的文件和文件夹名
print([d for d in os.listdir('.')])

#可以使用两个变量生成list
d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

#将list中的字符转为小写
L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])


#homework,数字不让其转换
L2 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L2 if isinstance(s,str)])
print([s.lower() for s in L2 if isinstance(s,str)])#如何让数字不会被去除呢？

