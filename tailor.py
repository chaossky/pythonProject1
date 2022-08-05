import math

def func_e(x, n):
    e_approx = 0.0
    for i in range(n):
        e_approx += x**i/math.factorial(i)
    
    return e_approx
    
x = 1.0

for i in range(1,21):
    e_approx = func_e(x,i)
    e_exp = math.exp(x)
    e_error = abs(e_approx - e_exp)
    print(f'{i} terms: Taylor Series approx= {e_approx}, exp calc= {e_exp}, error = {e_error}')
