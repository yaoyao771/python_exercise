#encoding:utf-8
def generateParenthesis(n):

    answer=[]
    r,l=n,n
    while r!=0 and l!=0:
        s=''
        if r==l:
            s=s+'('
            r-=1
        if r>0:
            s+='('
            r-=1
        if r<l:
            s=s+')'

    answer.append(s)