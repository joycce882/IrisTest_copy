# 写一段代码，实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
# 例如把 9 表示成二进制是 1001，有 2 位是 1。因此如果输入 9，该函数输出 2。


def count_one(n):
    count = 0
    while n:
        n = n & (n - 1)
        count += 1
    return count


print(count_one(5))

