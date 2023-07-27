#一、根据运动员得分，找到相对等级和获得最高分前三名的人，分别获得金牌、银牌和铜牌。N是整数，并且不超过10000.所有运动员的成绩都保证是独一无二的
#二、问题示例：输入[5,4,3,2,1],输出["gold medal","silver Medal","bronze medal","4","5"],前3名运动员得分较高，根据得分依次获得金牌、银牌、铜牌。对于后两名运动员，根据分数输出相对等级
#方案一
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


