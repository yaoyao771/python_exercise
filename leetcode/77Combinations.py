'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
'''


def combine( n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    res = []
    if n < 0 or n < k:
        return res
    dfs(n, k, 1, [], res)
    return res


def dfs( n, k, start, ans, res):
    if len(ans) == k:
        res.append(ans[:])

    index = n + 1
    for i in range(start, index):
        ans.append(i)
        dfs(n, k, i + 1, ans, res)
        ans.remove(i)
n=4
k=2
combine(n,k)
