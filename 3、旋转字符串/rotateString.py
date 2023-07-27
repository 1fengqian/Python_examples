#一、给定一个字符串（以字符数组的形式）和一个偏移量，根据偏移量原地从左向右旋转字符串
def rotate_string(s, offset):
    offset = offset % len(s)
    def reverse(start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    reverse(0, len(s) - 1)  # 翻转整个字符串
    reverse(0, offset - 1)  # 翻转前offset个字符
    reverse(offset, len(s) - 1)  # 翻转剩余的字符

if __name__ == "__main__":
    # 测试示例
    s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    offset = 4
    rotate_string(s, offset)
    print(s)  # 输出：['d', 'e', 'f', 'g', 'a', 'b', 'c']
#方案二
class Solution:
    #参数s:字符列表
    #参数offset:整数
    #返回值:无
    def rotateString(self, s, offset):
        if len(s) > 0:
            offset = offset % len(s)
        temp = (s + s)[len(s) - offset : 2 * len(s) - offset]
        for i in range(len(temp)):
            s[i] = temp[i]
#主函数
if __name__ == '__main__':
    s = ["a","b","c","d","e","f","g"]
    offset = 3
    solution = Solution()
    solution.rotateString(s, offset)
    print("输入：s =", ["a","b","c","d","e","f","g"], " ", "offset =",offset)
    print("输出：s =", s)




