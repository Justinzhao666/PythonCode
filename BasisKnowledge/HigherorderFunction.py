from math import sqrt
from functools import reduce
#函数当参数
f = abs
def add(x,y,f):
	return f(x)+f(y)

print(add(-2,-1,f))



#demo
print('*****************************')
def demo(x,*fs):
	return [f(x) for f in fs]# 既然函数名也是变量，那么我们自然可以对一个函数名的容器进行迭代

print(demo(2,sqrt,abs))

#map
print('*****************************')
def function(x):
	return x*x
r = map(function,[1,2,3,4,5])
print(list(r))



#reduce
print('*****************************')

def add(x,y):
	return x+y
list_to_add = [1,2,3,4,5]
print(reduce(add,list_to_add))

print('*****************************')
#将 1，2，3，4转换为1234
def number(x,y):
	return x*10+y
list_1 = [1,2,3,4]
print(reduce(number,list_1))



#将string转int的
print('*****************************')
def to_int(x):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9} [x]  #很高级的用法啊：{}[]   dict的取值方式
def str_to_int(list_str):
	list_2 = list(map(to_int,list_str))
	return reduce(number,list_2)
print(str_to_int('12345'))



print('****************练习*************')
list_3 = ['adam', 'LISA', 'barT']
def normalize(name):
	return name[0].upper()+name[1:].lower()  #唉，前学后忘---切片！

print(list(map(normalize,list_3)))


list_4 = [3, 5, 7, 9]
def prod(L):
	return reduce(lambda x,y: x*y, L)
print('3 * 5 * 7 * 9 =', prod(list_4))

def to_num(x):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'} [x]
def addAll1(x,y):
	return x*10+y
def addAll2(x,y):
	return x/10+y
def returnlist(L):
	newL = []
	newL1 = []
	for var in L:
		if(var == '.'):
			newL.append(newL1)
			newL1 = []
			continue
		else:
			newL1.append(var)

	newL.append(newL1[::-1])		#数组倒置，只能说我对切片掌握还不够
	return newL

def str2float(s):	
	list_5 = returnlist(list(map(to_num,s)))
	result = reduce(addAll1,list_5[0]) + reduce(addAll2,list_5[1])/10
	return result

print('str2float(\'123.456\') =', str2float('123.456'))


print('*****************************')
#using build_in function
def toFloat(s):
	s1 = s.split('.')#就是对内置函数的不熟悉导致这样的情况  分隔函数
	return reduce(addAll1,(map(to_num,s1[0])))+reduce(addAll1,list(map(to_num,s1[1])))/(10**len(s1[1])) # **表示次方
# reduce 好像传入一个iterator也是可以的，或者说reduce本身就会做自动迭代，对Iterator进行取值--应该是这样的！
print('toFloat(\'123.456\') =', toFloat('123.456'))