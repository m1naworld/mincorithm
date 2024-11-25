'''
선택해서 정렬한다.

시간복잡도: O(N^2)
'''

'''
Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 오름차순으로 선택 정렬을 이용해서 정렬하시오.
'''


input = [4, 6, 2, 9, 1]


def selection_sort(array):

    # 총 시간 복잡도: O(N^2)
    for i in range(len(array)): # O(N)
        min_num_index = 0
        for j in  range(1 + i , len(array)): # O(N)
            if array[j] < array[min_num_index]:
                min_num_index = j
        array[i], array[min_num_index] = array[min_num_index], array[i]
    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))