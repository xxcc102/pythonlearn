class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        rst = []
        odd = []
        even = []

        for a in A:
            if a%2 == 0:
                odd.append(a)
            else:
                even.append(a)

        for i in range(len(A)):
            if i%2 == 0:
                rst.append(odd.pop())
            else:
                rst.append(even.pop())
        print(rst)

        '''
        rst = []
        for i in range(len(A)):
            if A[i]%2 == 0:
         '''
        print(rst)

if __name__ == "__main__":
    sol = Solution()
    A = [4,2,5,7]
    B = sol.sortArrayByParityII(A)
    print(B)