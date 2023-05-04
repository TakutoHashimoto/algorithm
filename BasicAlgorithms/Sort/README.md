# ソートのアルゴリズム
**太字**のものは重要
* Bogoソート
* **Bubbleソート**
    * Cocktailソート（カクテルソート、シェーカーソート）
    * Combソート
    * **Selectionソート（選択法）**
    * Gnomeソート
* **Insertionソート（挿入法）**
    * Bucketソート
    * Shellソート
* Countソート
    * Radixソート
* **Quickソート**
* **Mergeソート**
* **Heapソート**
* Timソート
    * insertionソートとmergeソートを使用している


## 各アルゴリズムの計算量と安定性
* 計算量と安定性については後述

| Sort | Ave | Best | Worst | Stable | Comment |
| :---: | :---: | :---: | :---: | :---: | :--- |
| bogo | $O((n+1)!)$ | $O(n)$ | Unbound | No | - |
| **bubble** | $O(n^2)$ | $O(n)$ | $O(n^2)$ | Yes | - |
| cocktail | $O(n^2)$ | $O(n)$ | $O(n^2)$ | Yes | - |
| comb | $O(n^2/2^g)$ | $O(n \log{n})$ | $O(n^2)$ | No | * bubble sortの改良 <br> * $g$: number of a increment|
| **selection** | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | Yes | bubble sortの改良 |
| gnome | $O(n^2)$ | $O(n)$ | $O(n^2)$ | Yes | bubble sortに類似 |
| **insertion** | $O(n^2)$ | $O(n)$ | $O(n^2)$ | Yes |  |
| bucket | $O(n+k)$ | $O(n+k)$ | $O(n^2)$ | Yes | insertion sortを使用 |
| shell | Depends on gap sequence | $O(n \log{n})$ | $O(n^2)$ | No | insertion sortの改良 |
| count | $O(n)$ | $O(n)$ | $O(n)$ | Yes |  |
| radix | $O(n)$ | $O(n)$ | $O(n)$ | Yes | count sortを使用 |
| **quick** | $O(n \log{n})$ | $O(n \log{n})$ | $O(n^2)$ | No |  |
| **merge** | $O(n \log{n})$ | $O(n \log{n})$ | $O(n \log{n})$ | Yes |  |
| **heap** | $O(n \log{n})$ | $O(n \log{n})$ | $O(n \log{n})$ | No |  |
| tim | $O(n \log{n})$ | $O(n)$ | $O(n \log{n})$ | Yes | insertion sortとmerge sortを使用 |


## 計算量について
* Big O Notation
* 計算量が少ない順に、$O(1) < O(\log{n}) < O(n) < O(n \log{n}) < O(n^2)$ となる。
* 以下は各計算量のサンプルコード
    ```python
    # O(1)
    def func1(numbers: list):
        return numbers[0]


    # O(log(n))
    def func2(n: int):
        if n <= 1:
            return
        else:
            print(n)
            func(n/2)


    # O(n)
    def func3(numbers: list):
        for num in numbers:
            print(num)


    # O(n*log(n))
    def func4(n: int):
        for i in range(n):
            print(i, end=' ')
        print()

        if n <= 1:
            return
        func4(n/2)


    # O(n**2)
    def func5(numbers: list):
        for i in range(len(numbers)):
            for j in range(len(numbers)):
                print(numbers[i], numbers[j])
            print()
    ```

## 安定性について
* ソート判定において、同一と判断された入力データの順序がソート後も変わらない

### Stable Sort
```python
l = [
    (1, 'Mike'),
    (5, 'Rina'),
    (2, 'Bill'),
    (4, 'Emily'),
    (2, 'June')
]


def stable(l: list):
    l[1], l[2] = l[2], l[1]
    l[2], l[4] = l[4], l[2]
    return l


print(l)
# => [(1, 'Mike'), (2, 'Bill'), (2, 'June'), (4, 'Emily'), (5, 'Rina')]
```

### Unstable Sort
```python
l = [
    (1, 'Mike'),
    (5, 'Rina'),
    (2, 'Bill'),
    (4, 'Emily'),
    (2, 'June')
]


def unstable(l: list):
    l[1], l[4] = l[4], l[1]
    return l


print(l)
# => [(1, 'Mike'), (2, 'June'), (2, 'Bill'), (4, 'Emily'), (5, 'Rina')]
```