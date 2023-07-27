#一、合并两个升序的整数数组A和B，形成一个新的数组，新数组也要有序
class Solution:
    def mergeSortArray(self,A,B):
        i,j = 0,0
        C= []
        while i<len(A) and j<len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i+=1
            else:
                C.append(B[j])
                j+=1
        while i<len(A):
            C.append(A[i])
            i+=1
        while j<len(B):
            C.append(B[j])
            j+=1
        return C
if __name__ == "__main__":
    A = [1,3,4,5,7]
    B = [2,6,9,67,89,90]
    print(A,B)
    solution = Solution()
    result = solution.mergeSortArray(A,B)
    print(result)







