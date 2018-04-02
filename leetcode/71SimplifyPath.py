'''
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
'''


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        lpath = [x for x in path.split('/') if x != '.' and x != '']
        res = []
        len_lpath = len(lpath)
        for i in range(len_lpath):
            if lpath[i] == '..':
                if i > 0:
                    res = res[:-1]

            else:
                res.append(lpath[i])
        return '/' + '/'.join(res)

