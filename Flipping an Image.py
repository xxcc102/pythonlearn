class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rstin = []
        rstout = []
        A.reverse()
        for i in A:
            i.reverse()
            for j in i:
                rstin.append(abs(j - 1))
            rstout.append(rstin.copy())
            rstin.clear()
        return rstout


if __name__ == "__main__":
    a = [[1,1,0],[1,0,1],[0,0,0]]
    sol = Solution()
    b = sol.flipAndInvertImage(a)
    print(b)