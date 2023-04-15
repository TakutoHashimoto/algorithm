def convert(S :str) ->int:
    '''
    文字列を数値に変換する
    '''
    # 先頭の文字がマイナスになっているかどうか
    if S[0] == '-':
        top = 1
    else:
        top = 0
