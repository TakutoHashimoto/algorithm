def is_leap_year(year :int) ->bool:
    '''
    yearがうるう年か判定する
    '''
    if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap_year(year))
