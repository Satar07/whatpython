# python的流程控制

##  if语句

`if` 语句最简单的构成是这样的：

```python
if SomethingHappen:
    DoThisCode
```

> 注意第 1 行末尾的冒号 : 和第 2 行的 4 个空格缩进

除此之外，Python 还加入了 `elif`，即 `else if`，方便执行更复杂的判断。

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190521-1558431295427)

**如：**买 2 个西瓜，4 个苹果，5 根香蕉

代码如下（示例，非标准代码） ：

```python
if 看到卖西瓜的:    #当满足条件时，执行内部的代码；如不满足，则跳到下一个语句块
    买 2 个
elif 看到卖苹果的:
    买 4 个
elif 看到卖香蕉的:
    买 5 根
else:   # 如果上面的条件都不满足，则执行 else 内部的代码
    不买
```

**以下内容必须重视**

- if、elif、else 后要加冒号 `:`，告诉计算机这是一个判断语句，如满足条件，就执行语句块内部的代码。
- Python 使用严格的缩进，来区分代码块的执行级别。比如 if 下面的代码要缩进四个空格，代表的是 if 内部的功能；else 下面的代码同样要缩进四个空格，代表是 else 内部的功能。
- 推荐使用 4 个空格缩进；也可以在编辑器内，把 `Tab` 键改为四个空格，用 `Tab` 键缩进。
- 用 `input()` 接受到的用户输入，类型为字符串 `string`，但字符串不能和整数比较大小，所以要用 `int()` 函数将数据转换为 `int` 整数类型。
- 使用 `int()` 函数，可以把括号里的内容转换为整数，但要注意：只有数字或纯数字的字符串才能转换，如'a'、'abc'这样的内容就不行；float 类型的数字会只保留整数部分。

**还可以使用 and 和 or 进行综合控制**：

```python
if 那个人是女人 and 单身:   # A 和 B必须同时满足才能执行
    你可以追求她
else：
    成为基友
```

## 循环

Python 中包含两种循环方式，一种是 `for 循环`，一种是 `while 循环`。

![循环控制](https://doc.shiyanlou.com/courses/uid8504-20190522-1558511158849)

### for 循环

**for循环主要用于对一个范围内的每个元素进行指定操作。**

`for` 循环适用于 **已知循环次数** 的循环，所以后面跟的是次数或区间，到达指定次数就停止。

语法如下：

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190604-1559632549800)

比如在一个班级里，点名册就是一份列表，每个姓名都是一个元素。现在你是班长，每天上课前的点名太费劲了，你需要一个点名程序。

用 `for` 循环，2 行代码即可实现该功能：

```python
namelist = ['Sophia','Emma','Olivia','Ava','Mia','Isabella','Zoe','Lily','Emily','Madison','Jackson','Aiden','Liam','Lucas','Noah','Mason','Ethan','Caden','Logan','Jacob']
# 点名册
for i in namelist:
    print(i)
```

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190522-1558514369488)

### range() 函数

如果需要处理一组数字列表，并且数字列表满足一定的规律，可以使用 Python 的内置函数 `range()`（范围）。

使用 `range(x)` 函数，可以生成一个从 0 到 x-1 的整数序列，比如我们想打印 0 到 9 的数，可以这样写：

```python
for a in range(10):
    print(a)
```

还可以用 `range(a,b)` 取某个区间的数，比如要打印 1 到 10 ,你可以写：

```python
for a in range(1,11):
    print(a)
```

> 注意： `range(a,b)` 包头不包尾，尾数要 + 1 。

### while循环

`while` 后面跟的是一个条件，只要条件满足，这个循环就会一直进行下去。

具体语法如下：

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190604-1559632814963)

有了 `while 循环` ，愚公可以这样移山：

```python
while 山还在:
    盘它！
```

### 再总结一下两种循环的区别：

![图片描述](https://doc.shiyanlou.com/courses/uid8504-20190522-1558516464511)

### break

在循环中，我们可以使用 `break` 和 `continue` 这两个关键字，来进一步控制流程。

`break` 表示停止当前循环，如：

```python
for a in range(10):
    if a == 5:
        break
    print(a)
```

程序会打印 0 到 4 之间的数字。

### continue

`continue` 表示跳过当前循环轮次，去执行下一轮循环。

比如这次我们想打印 1 到 10 的数，但不想打印 5 ，代码可以这样写：

```python
a = 0
while a < 10:
    a = a + 1
    if a == 5:
        continue
    print(a)
```

## 总结

![](https://labfile.oss.aliyuncs.com/courses/1330/python2.png)