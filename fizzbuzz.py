class Solution(object):
    def fizzbuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1,n+1):
            if i% 3== 0 and i%5==0:
                result.append("FizzBuzz")
            elif i %3==0:
                result.append("fizz")
            elif i %5==0:
                result.append("buzz")
            else:
                result.append(str(i))
        return result
ob1 = Solution()
print(ob1.fizzbuzz(100))
