def gcd(a :int, b :int) ->int:
    '''
    aとbの最大公約数を求める
    '''
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    
    return a

a, b = map(int, input().split())
print(gcd(a, b))
