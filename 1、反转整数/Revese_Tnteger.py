#实例一、反转一个只有三位数的整数
#方案一
#定义一个函数：首先判断输入的是否为一个三位数，然后将整数转换为字符串，并进行翻转
def reverse_integer(num):
    if num < 100 or num > 999:
        raise ValueError("Input must be a 3-digit number.")
    # 将整数转换为字符串，并进行翻转
    reversed_str = str(num)[::-1]
    # 将翻转后的字符串转换回整数
    reversed_num = int(reversed_str)
    return reversed_num

if __name__ =='__main__':
    num = 123
    reversed_num = reverse_integer(num)
    print(f"原始数字：{num}")
    print(f"翻转后的数字：{reversed_num}")
#方案二
class Solution:
    def reverseInteger(self, number):
        h = int(number/100)
        t = int(number%100/10)
        z = int(number%10)
        return (100*z+10*t+h)
#主函数
if __name__  ==  '__main__' :
    solution = Solution()
    num = 123
    ans = solution.reverseInteger(num)
    print("输入:", num)
    print("输出：", ans)


