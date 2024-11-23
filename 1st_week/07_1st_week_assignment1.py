'''
Q. 링크드 리스트의 '끝'에서 K번째 값을 반환하시오.

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

    # 1. 우선 모든 LinkedList 의 길이를 구한다.
    # 2. LinkedList의 길이에서 K만큼 빼고, 그만큼 이동시킨다.
    # 3. 그 노드를 반환한다.
    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        length = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length += 1

        cur = self.head
        for index in range(length - k):
            cur = cur.next

        return cur

    # 개선편: 포인터 사용
    # K만큼의 길이가 떨어진 포인터 두개를 두고, 한칸씩 이동
    # 앞에 나선 포인터가 끝에 도달하면, K만큼 뒤떨어진 포인터는 바로 끝에서 K번째의 값
    def get_kth_node_from_last_pointer(self, k):
        follow_pointer = self.head
        ahead_pointer = self.head

        for i in range(k):  # k만큼 떨어진 노드 찾기
            ahead_pointer = ahead_pointer.next

        while ahead_pointer is not None:
            follow_pointer = follow_pointer.next
            ahead_pointer = ahead_pointer.next

        return follow_pointer



linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last_pointer(2).data)

'''
시간 복잡도 측면

둘다 결국 링크드 리스트의 끝까지 가야 하므로 같은 O(N) 의 성능을 가짐.
게다가, 생각해보면 두 개의 공간값을 가지고 이동해야 하므로 비슷하게 연산량을 사용.
(물론 N이 매우 커지면 2N과 N이라 차이가 나긴 함!)
따라서, 두 번 도는 것보다 한 번 도는 게 무조건 빠르다고는 생각하지 말자! 
'''