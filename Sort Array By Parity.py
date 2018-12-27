class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        oddlist = []
        evenlist = []
        for i in A:
            if i%2 == 0:
                oddlist.append(i)
            else:
                evenlist.append(i)
        oddlist.extend(evenlist)
        print(oddlist)
        return oddlist

            
if __name__ == "__main__":
    sol = Solution()
    A = [3,1,2,4]
    B = sol.sortArrayByParity(A)
    print(B)