# Bài 01: Viết một chương trình Python in ra dãy số Fibonacci
# Gợi ý:
# Sử dụng đệ quy
# Không sử dụng đệ quy
def fibonacci_nonRecur(n)->list:
    """
    ham tra ve list [] day so fibonacci f0,f1,f2,.....fn
    ham su dung vong lap for tinh va nap cac gia tri vao list []
    n<0 tra ve [-1]
    fibonacci_nonRecur(10) = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    fib=[]
    if n <0:
        return [-1]
    if n == 0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        fib=[0,1]
        for i in range(2,n+1):      
            fib.append(fib[i-1]+fib[i-2])
        return fib
def fibonacci_Recur(n)->list:
    """
    ham tra ve list [] day so fibonacci f0,f1,f2,.....fn
    ham su dung de quy tinh va nap cac gia tri vao list []
    n<0 tra ve [-1]
    fibonacci_Recur(10) = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    fib=[]
    def __run_Recur(n):
        if n<0:
            return -1
        elif n==0:
            return 0
        elif n==1 or n==2:
            return 1
        return __run_Recur(n-1)+__run_Recur(n-2)
    for i in range(0,n+1):
        fib.append(__run_Recur(i))
    return fib

def HaNoitower(n,a,b,c)->list:
    """       a  -------->   b      -------->   c        
           ///////           H                  H
        ///////////          H                  H
      //////////////         H                  H
    //////////////////       H                  H
    nếu có 1 đĩa :
        a ------->b
    nếu có n đĩa:
        (n-1) ----------------------------->    c
         a----------------> b
                            b <-------------  (n-1)
        plan = HaNoitower(3,1,2,3) with n= 3, col 1, col 2, col 3
    """
    __plan_sub=[]
    def __movetower__(h,c1,c2,c3):
        if h==1:  
            __plan_sub.append([c1,">>",c2])
        else:
            __movetower__(h-1,c1,c3,c2)
            __plan_sub.append([c1,">>",c2])
            __movetower__(h-1,c3,c2,c1)
    __movetower__(n,a,b,c)
    return __plan_sub

if __name__=="__main__":
    # # print(fibonacci_nonRecur.__doc__)
    # print(fibonacci_nonRecur(10))
    # # print(fibonacci_Recur.__doc__)
    # print(fibonacci_Recur(10))
    plan =HaNoitower(4,1,2,3)
    for i in plan:
        print(i)



