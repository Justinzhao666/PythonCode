from functools import reduce
#去除序列中的空字串
def is_empty(s):
	return s and s.strip()		#本身就是空的'' 和里面是空格字串的' ' 都要去除
list1 = list(filter(is_empty, ['A', '', 'B', None, 'C', '  ']))
print(list1)


#filter求素数
#产生一连串的数字序列， 生成奇数！ 我也是笨，偶数（一定能被2除）当然不会是素数！ 素数一定是奇数除了2之外
def number_builder():
	n= 1
	while True:
		n = n+2
		yield n
#判断是否为素数
def is_prime(n):
	return lambda x: x%n >0	#这个还是没有懂？？？？？？？？？？？？？
#
def prime():
	yield 2
	it = number_builder()
	while True:
		n = next(it) #取出新序列的第一个元素，那就是素数---应为他坑定不能被在它之前的所有数整除
		yield n   #函数遇到yield就返回了，被调用next的时候会接着下面执行  这里的n必定是素数
		it = filter(is_prime(n),it)  #这时候it已经改变了 和numberbuild（）已经不是一个性质了  得到一个新序列
		#！！每一次执行这个步骤的目的不是为了生成素数序列，而是让该序列第一个数为素数 = 除以最新的n 能保留的一定是素数！而且每次next也只取第一个


#这种算法要注意： 新，旧序列不都是素数，而且是无限的。每次取得新序列第一个数才是素数！被打印出来了。

#理一下prime()流程：
# 1. 输出2
# 2. 获得奇数序列迭代器
# 3. 进入循环，取3 打出3
# 4. 将it的序列全部除以3，如果可以除尽那么就it中去除
# 	---这里就是我最疑惑的地方：it是个无限序列，会全部除？怎么能除尽啊！
# 	---我想多了 filter是个惰性序列，那么对it的处理也是惰性的，当有人要取filter的时候，filter才会去取it的，it会被is_prime()过滤。
# 	---内部一定是两种方案，it存储一定数据用于操作，超出范围无效；一种机制将过滤规则记住叠加到后期处理上；
# 	---核心
# 		---filter(....)能保证序列的第一数是素数，以及新序列里面的数都不能被n前面的数整除！

# # 那么问题来了：怎么生成素数？
# 	---对每一个数都把它之前的数除一遍，都除不尽肯定是素数！（1，本身这些除外）
# 	---再优化：1、先去除偶数（2除外） 2、将这之前的素数都保存，去除这些素数，都不能整除就是素数
# 	---素数的个数是有限的有个素数表。

for var in prime():
	if var < 100:
		print(var)
	else:
		break

print('_________homework__demo 回数_______________')

def addAll(x, y):
	return 10 * x + y

def is_palindrome(n):
	L = []
	tmp = n
	while n:
		L.append(n%10)
		n = n//10
	return reduce(addAll,L) == tmp


print(reduce(addAll,[1]))

output = filter(is_palindrome, range(1, 1000))
print(list(output))

# 使用内置函数方法
def is_palindrome2(n):
	return str(n) == str(n)[::-1]
output = filter(is_palindrome2, range(1, 1000))
print(list(output))