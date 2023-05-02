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


## 安定性について