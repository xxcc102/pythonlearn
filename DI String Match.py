class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        for w in S:
            if w == "I":

                pass
            elif w== "D":
                pass


if __name__ == "__main__":
    a = "IDID"
    sol = Solution()
    b = sol.diStringMatch(a)
    print(b)

