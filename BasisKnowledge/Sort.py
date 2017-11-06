
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key=by_name)
L3 = sorted(L,key=by_score,reverse=True)
print(L2)
print(L3)

a,b,c = [1,2,3]
print(a)
print(b)
print(c)


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         fs.append(f)
#         print(f)
#     return fs


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        # print(f(i))
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
print(f1.__name__,f2.__name__,f3.__name__)  #函数对象的一个属性，可以打印出对象引用的函数名


