#encoding:utf-8
def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    MAX_INT = 2147483647
    if divisor == 0:
        return MAX_INT
    if dividend == 0:
        return 0
    sign = 1
    if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        sign = -1
    dividend, divisor = abs(dividend), abs(divisor)
    maps = [divisor]
    times = [1]

    i = 0
    while dividend >= maps[i]:
        i += 1
        maps.append(maps[i - 1] + maps[i - 1])
        times.append(times[i - 1] + times[i - 1])
    j, sums = i - 1, 0
    while j >= 0:
        if maps[j] < dividend:
            dividend -= maps[j]
            sums += times[j]
            j -= 1
    if sign == 1:
        return sums
    else:
        return -sums

'''
def divide( dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        


        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

'''

