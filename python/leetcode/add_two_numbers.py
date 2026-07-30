class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = ListNode(value=nodes.pop(0))

            self.head = node

            for element in nodes:
                node.next = ListNode(value=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.value)
            node = node.next

        return str(nodes)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next


class Solution:
    def addTwoNumbers(
        self, list1: LinkedList | None | list, list2: LinkedList | None | list
    ) -> LinkedList | None:
        if type(list1) is not LinkedList:
            list1 = LinkedList(list1)

        if type(list2) is not LinkedList:
            list2 = LinkedList(list2)

        arr_of_list_1 = []
        arr_of_list_2 = []

        if list1 is not None:
            for node in list1:
                arr_of_list_1.append(node.value)

        if list2 is not None:
            for node in list2:
                arr_of_list_2.append(node.value)

        print(arr_of_list_1)
        print(arr_of_list_2)

        arr_of_list_1.reverse()
        arr_of_list_2.reverse()

        int_of_list_1 = 0
        int_of_list_2 = 0

        for num in arr_of_list_1:
            int_of_list_1 = int_of_list_1 * 10 + num

        for num in arr_of_list_2:
            int_of_list_2 = int_of_list_2 * 10 + num

        total_sum_of_linked_lists = int_of_list_1 + int_of_list_2

        reversed_total_sum = int(str(total_sum_of_linked_lists)[::-1])

        reversed_total_sum_list = [int(digit) for digit in str(reversed_total_sum)]

        return LinkedList(reversed_total_sum_list)


solution_instance = Solution()

# Test case 1
data_case_1 = [2, 4, 3]
data_case_2 = [5, 6, 4]

# We first need to create the Linked List, as we only have the solution and ListNode

print(solution_instance.addTwoNumbers(data_case_1, data_case_2))

# Test case 2
linked_list_ln1 = [0]
linked_list_ln2 = [0]

# Test case 3
linked_list_lc1 = [9, 9, 9, 9, 9, 9, 9]
linked_list_lc2 = [9, 9, 9, 9]
