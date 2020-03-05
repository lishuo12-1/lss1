a=[1,2,4,5,6,7,3,7,3,5,8,86,2,]
def fn(a):
    return a%2==1
newlist=filter(fn,a)
newlist=[i for i in newlist]
print(newlist)



# 自定义异常用raise抛出异常
def fn():
    try:
        for i in range(5):
            if i>2:
                raise Exception("数字大于2了")
    except Exception as b:
        print(b)
fn()

try:
    a
except IndexError as e:
    print(e)
    print(type(e))
    # a = 0
except NameError as e:
    print(a)
    print(e)
except Exception as e:
    print(e)
else:
    print('没异常。。。。。')
finally:
    print('finally.....')


class Myclass(Exception):
    def __init__(self, msg='我的自定义异常'):
        self.msg = msg

    def __str__(self):
        return self.msg



m = Myclass('ssssssssss')
raise m

# IOError：输入输出异常
#
# AttributeError：试图访问一个对象没有的属性
#
# ImportError：无法引入模块或包，基本是路径问题
#
# IndentationError：语法错误，代码没有正确的对齐
#
# IndexError：下标索引超出序列边界
#
# KeyError：试图访问你字典里不存在的键
#
# SyntaxError：Python代码逻辑语法出错，不能执行
#
# NameError：使用一个还未赋予对象的变量