#encoding:utf-8

def longestcommonprefix(strs):


        result = ''
        if len(strs)==0:
            return ""

        else:
            s_len=len(strs[0])
            for i in range(1,len(strs)):

                s_len=min(s_len,len(strs[i]))
            print(s_len)
            for j in range(s_len):
                a=strs[0][j]
                for k in range(1,len(strs)):
                    if strs[k][j]!=a:
                        print(result)
                        return result
                result+=a
        print( result)
strs=['abcd','abc','ab','abd']
longestcommonprefix(strs)



