#encoding:utf-8

def longestPalindrome( s):
        """
        :type s: str
        :rtype: str
        """
        a = list(s)
        b = [1]
        length = len(a)
        for i in range(1,length):
            c = 1
            if a[i] == a[i-1]:
                c += 1
                if i > 1:
                    for j in range(min(i, length - i)):
                        if a[i - j-i] == a[i + j]:
                            c += 2
                        else:
                            break
                else:
                    break



            if a[i] != a[i -1]:
                if i!=length-1:
                    for j in range(1, min(i, length - i )+1):
                        if a[i - j] == a[i + j]:
                            c += 2
                        else:
                            break
                else:
                    c=1
            b.append(c)
        print(b)
        max_len = max(b)
        max_index =b.index(max(b))
        print (max_index)
        if max_len % 2 == 0:
            max_list = a[max_index - int(max_len) / 2:max_index + int(max_len / 2)]
        else:
            max_list = a[max_index - int(max_len / 2):max_index +int(max_len/2)+1]
        k="".join(max_list)
        print (k)

s="babad"
longestPalindrome(s)

 #       return max_list