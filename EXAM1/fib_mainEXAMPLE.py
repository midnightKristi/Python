from fib import *

def main():
    print(is_fib_like([]))
    print(is_fib_like([42]))
    print(is_fib_like([18,42]))
    print(is_fib_like([1,1,1]))
    print(is_fib_like([1,2,3]))
    print(is_fib_like([0,0,0,0,0]))
    print(is_fib_like([1,1,2,3,5,8,13,21]))
    print(is_fib_like([2,1,3,4,7,11,18,29]))
    print(is_fib_like([1,1,2,3,512,17]))

main()
