class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mi = min(m-1, n-1)
        if not mi:
            return 1
        else:
            methods = 1
            for i in range(mi):
                methods *= (m+n-2-i)
            for i in range(mi):
                methods = methods//(i+1)   #全是整型
            return methods
