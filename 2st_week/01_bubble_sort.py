'''

버블 정렬이란?
두 인접한 데이터의 크기를 비교하고, swap 연산을 수행하며 정렬하는 방식
쉽게 말해, 첫 번째 자료와 두 번째 자료를, 두 번째 자료와 세 번째 자료를, 세 번째와 네 번째를, … 이런 식으로 (마지막-1)번째 자료와 마지막 자료를 비교하여 교환하면서 자료를 정렬하는 방식
*시간복잡도는 O(n^2)

- Swap 하는 방법
두 변수의 값을 교체 하려면 다른 언어에서는 임시로 값을 저장해두는 변수를 따로 둬야함.
그러나 파이썬에서는 쉽게 구현 가능
a, b = b, a
'''


'''
Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 버블 정렬을 이용해서 정렬하시오.

'''

input = [4, 6, 2, 9, 1]

def bubble_sort_me(array):
    need_length = len(array)
    for i in range(need_length -1):
        for j in range(need_length - 1):
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        need_length -= 1  # 불 필요한 연산을 추가적으로 진행 ㅠ,ㅠ

    return array

def bubble_sort_dingco(array):
    n = len(array)
    for i in range(n -1):
        for j in range(n - i - 1): # Good!
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array


bubble_sort_me(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort_me([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort_me([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort_me([100,56,-3,32,44]))