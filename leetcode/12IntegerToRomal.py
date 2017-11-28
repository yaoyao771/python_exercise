#encxoding:utf-8
def solution(num):
    '''
    s = str(num)
    s=s[::-1]
    num_digit = 0
    num_tens = 0
    num_hun = 0
    num_thou = 0
    if 0 < num < 4000:
        a=int(s[0])
        if 0 < a < 4:
            num_digit = str('I' * a)
        if 4 < a < 9:
            num_digit = str('V' + 'I' * (a % 5))
        if a == 4:
            num_digit = str('IV')
        if a==9:
            num_digit = str('IX')
        if a==0:
            num_digit=str('')
        answer=num_digit
        if num > 9:
            b=int(s[1])
            if 0 < b < 4:
                num_tens = str('X' * b+num_digit)
            if 4 < b < 9:
                num_tens = str('L' + 'X' * (b % 5)+num_digit)
            if b == 4:
                num_tens = str('XL'+num_digit)
            if b==9:
                num_tens = str('XC'+num_digit)
            if b==0:
                num_tens=answer
            answer=num_tens
            if num > 99:
                c=int(s[2])
                if 0 < c < 4:
                    num_hun = str('C' * c + num_tens)
                if 4 < c < 9:
                    num_hun = str('D' + 'C' * (c % 5)+num_tens)
                if c == 4:
                    num_hun = str('CD'+num_tens)
                if c==9:
                    num_hum = str('CM'+num_tens)
                if c==0:
                    num_hun=num_tens

                answer=num_hun

                print (answer)
                if num > 999:
                    d=int(s[3])
                    num_thou = str('M' * d+num_hun)
                    answer=num_thou
    '''

#    answer = (num_thou) + (num_hun) + (num_tens) + (num_digit)
 #           print(answer)
#num=101

    roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
                     ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                     ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], ["", "M", "MM", "MMM"]]
    res = []
    res.append(roman[3][int(num / 1000 % 10)])
    res.append(roman[2][int(num / 100 % 10)])
    res.append(roman[1][int(num / 10 % 10)])
    res.append(roman[0][int(num % 10)])
    s= "".join(res)
    print (s)


solution(1090)
