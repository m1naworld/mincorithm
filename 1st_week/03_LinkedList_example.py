'''
두 링크드 리스트의 합 계산

Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.

예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
각각 678, 354 이므로 두개의 총합
678 + 354 = 1032 를 반환해야 한다.

단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):
    num_1 = get_linked_list_num(linked_list_1)
    num_2 = get_linked_list_num(linked_list_2)

    return num_1 + num_2

def get_linked_list_num(linked_list):
    cur = linked_list.head
    num = linked_list.head.data

    while cur.next is not None:
        cur = cur.next
        num = num * 10 + cur.data

    return num


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))