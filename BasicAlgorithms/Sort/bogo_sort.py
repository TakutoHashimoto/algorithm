import random

# 型ヒント
from typing import List

def is_in_order(numbers: List[int]) -> bool:
    '''
    リストの要素が昇順になっているかチェックする
    '''
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # 上の処理は下に書いてあるものと同じことをやっている
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    
    # return True

def bogo_sort(numbers: List[int]) -> List[int]:
    '''
    リストをシャッフルして要素を並び替える
    '''
    while not is_in_order(numbers):
        # リストの要素が昇順になっていない間はシャッフルをし続ける
        random.shuffle(numbers)

    return numbers

if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(nums))
