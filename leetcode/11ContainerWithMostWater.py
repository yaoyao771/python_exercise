#encoding:utf-8
def maxArea(height):
    max_area=0
    '''
    for i in range(len(height-1)):
        for j in range(i,len(height)):
            area=(j-i)*min(height[i],height[j])
            if area>max_area:
                max_area=area
                
    return height[index_1],height[index_2]
    '''
    '''
    l=len(height)
    max_are=0
    index_1=0
    index_2=l-1
    while max(height[index_1 + 1:index_2]) > min(height[index_1], height[index_2]):
        for i in range(0,l-1):
            for j in range(1,l-i):
                area=(l-j-i)*min(height[i],height[l-j])
                if area>max_area:
                    area=max_area
                    index_1=i
                    index_2=l-j
    '''
    l = len(height)
    print (l)
    max_area = (l - 1) * min(height[l - 1], height[0])
    print(max_area)
    i = 0
    j = l - 1
    '''
    if l > 2:
        for i in range(0, l - 1):

            while max(height[index_1 + 1:index_2]) > min(height[index_1], height[index_2]) :
                for j in range(1, l - i - 1):
                    area = (l - j - i) * min(height[i], height[l - j])
                    if area > max_area:
                        max_area = area
                        index_1 = i
                        index_2 = l - j
                print(max_area)
    '''
    '''
    i=0
    j=len(height)-1
    while i!=j:

        area = ( j - i) * min(height[i], height[ j])
        if area > max_area:
            max_area = area
            index_1 = i
            index_2 = l - j
        if max(height[i+1:j])<=
    '''
    while i<j:
        max_area=max(max_area,(j-i)*min(height[i],height[j]))
        if height[i]<height[j]:
            i+=1
        else:
            j-=1
    return max_area


height=[1,2,1]
maxArea(height)


