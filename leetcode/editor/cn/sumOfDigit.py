def sum_of_digit(n):
    '''
    n=112
    remainder f(n)=f(n/10)+n%10
    112=11+2 f(n-1)
    11=1+2
    :param n:
    :return:
    '''
    def sum_of_digit(n):
        assert n>=0 and int(n)==n, "your number is not positive integer"
        if n==0:
            return 0
        else:
            return sum_of_digit(int(n//10))+int(n%10)
    print(sum_of_digit(4))
