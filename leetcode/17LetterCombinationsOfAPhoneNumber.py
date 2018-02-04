#encoding:utf-8
class solution(object):
    '''
    digit=[
           ['a','b','c'],
           ['d','e','f'],
           ['g','h','i'],
           ['j','k','l'],
           ['m','n''o'],
           ['p','q','r','s'],
           ['t','u','v'],
           ['w','x','y','z']]
    '''
    digit = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g', 'h', 'i'],
        '5':['j', 'k', 'l'],
        '6':['m', 'n','o'],
        '7':['p', 'q', 'r', 's'],
        '8':['t', 'u', 'v'],
        '9':['w', 'x', 'y', 'z']}

    answer=[]
    '''
    if len(digits)==0:

        return 0
    else:
        len_1=len(digit[digits[0]])
        len_2=len(digit[digits[-1]])
        c=[]
        d=[]
        for i in range(len_1):

            for j in range(len_2):

                d.append(digit[digits[0]][i]+digit[digits[-1]][j])

        print (d)
digits=str(2)
LetterCombination(digits)
'''
    map = [" ", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    length = 0;
    res = []

    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        self.length = len(digits)
        self.res = []
        if self.length == 0: return self.res;
        tmp = ['' for i in range(self.length)]
        self.getLetterCom(0, digits, tmp)
        return self.res

    def getLetterCom(self, index, digits, tmp):
        if index >= self.length:
            letters = ''.join(tmp)
            self.res.append(letters)
            return
        digit = ord(digits[index]) - ord('0')
        for i in range(len(self.map[digit])):
            tmp[index] = self.map[digit][i]
            self.getLetterCom(index + 1, digits, tmp)







