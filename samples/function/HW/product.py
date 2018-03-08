#-*- coding: utf-8 -*-

def product(x,y=1,*num):
    #for n in num:
     #   pass
    if not isinstance(x,(int,float)):
        raise TypeError("x")
    return x*y

print(product())