# -*- coding: utf-8 -*-
import math

def quadratic(a,b,c):
    if not isinstance(a,(int,float)):
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise  TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')

#x1=[-b-√(b²-4ac)]/2a
#x2=[-b+√(b²-4ac)]/2a
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1=-c/b
            x2=x1
            return x1,x2
    else:
        if d<0:
            return '方程无根'
        else:
            x1=(-b+math.sqrt(d))/2/a
            x2=(-b-math.sqrt(d))/2/a
            return x1,x2

print('quadractic(2,3,1)=',quadratic(2,3,1))
print('quadractic(1,3,-4)=',quadratic(1,3,-4))

if quadratic(2,3,1)!=(-0.5,-1.0):
    print('测试失败')
elif quadratic(1,3,-4)!=(1.0,-4.0):
    print('测试失败')
else:
    print('测试成功')