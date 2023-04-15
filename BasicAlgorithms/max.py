def max_value(A :list) ->int:
    '''
    リストの最大値を求める
    '''
    # リストの先頭の値を仮の最大値する
    max = A[0]
    
    for i in range(1, len(A), 1):
        if A[i] > max:
            max = A[i]
    
    return max

A = list(map(int, input().split()))
print(max_value(A))
