class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.val

    def __str__(self):
        return str(self.val)


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = ListNode(val=nodes.pop(0))

            self.head = node

            for element in nodes:
                node.next = ListNode(val=element)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.val)
            node = node.next

        return str(nodes)

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node
            node = node.next


class Solution:
    def addTwoNumbers(
        self, list1: LinkedList | None, list2: LinkedList | None
    ) -> LinkedList | None:

        # We sort the linked list first
        print(list1)
        print(list2)

        # We received the non-empty ListNode

        # We sort the List Node

        # We add each number

        # We return the result as a Linked List or as a ListNode

        # return list_node


solution_instance = Solution()

# Test case 1
data_case_1 = [2, 4, 3]
data_case_2 = [5, 6, 4]

linked_list_1 = LinkedList(data_case_1)
linked_list_2 = LinkedList(data_case_2)

# We first need to create the Linked List, as we only have the solution and ListNode

print(solution_instance.addTwoNumbers(linked_list_1, linked_list_2))

# Test case 2
linked_list_ln1 = [0]
linked_list_ln2 = [0]

# Test case 3
linked_list_lc1 = [9, 9, 9, 9, 9, 9, 9]
linked_list_lc2 = [9, 9, 9, 9]
