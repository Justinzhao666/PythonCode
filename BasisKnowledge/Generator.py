g = (x*x for x in range(10))
print(next(g))
print(next(g))
for var in g:
	print(var)

#Fibonacci数列
def Fib(max):
	n,a,b = 0,0,1
	while n<max:
		print(b)
		tmp = b
		b = a+b
		a = tmp
		n = n+1 #记录多少次

		#写法2
		#a,b = b,a+b  等价于 t = (a,a+b) a=t[0] b=t[1]也是有一个临时变量
	return 'DONE'

Fib(5)

def Fib_Generator(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n = n+1
	return 'DONE'
# next方式获取 函数generator
print('_____________')
o = Fib_Generator(4)
print(next(o))
print(next(o))
print(next(o))
print('_____________')
# for方式获取
for var in Fib_Generator(3):
	print(var)

print('______杨辉三角_______')
#homework 杨辉三角形
def triangles():
	L = [1]
	while True:
		yield L
		L.append(0) 	#为了让后面可以相加而生成数
		L = [L[i]+L[i-1] for i in range(len(L))]
		# 我的思维太死了！ --首先有规律的list，首先就要想到可不可以用列表生成式去做
		#2、list生成式中 不只是in中的元素操作结果！	 --可以根据实际情况转换：
		#算法中要求 是上一轮的数字相邻两个相加之和，那么就是L[i]与L[i-1]，这里的公共一直在迭代的量是i，所以想想i在可以在哪获取的
		#for(int i =0;i<xx;i++) python里面没有这样的式子，但是可以通过 for var in range(xxx)来替代--range(xxx)就是++的那一堆序列

		#for 方式
		# L2 = [1]
		# for var in range(1,len(L)):
		# 	L2.append(L[var]+L[var-1])
		# L = L2

count = 0
for var in triangles():
	print(var)
	count = count+1
	if count == 10:
		break


