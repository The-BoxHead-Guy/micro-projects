class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:

        # Process the Linked List to get the list of nodes extracted
        # Then add them in reverse mode directly using 'insert()'
        arr_of_list_1 = []
        arr_of_list_2 = []

        while l1 is not None:
            arr_of_list_1.insert(0, l1.val)
            l1 = l1.next

        while l2 is not None:
            arr_of_list_2.insert(0, l2.val)
            l2 = l2.next

        # Get the integers of the list
        int_of_list_1 = 0
        int_of_list_2 = 0

        for num in arr_of_list_1:
            int_of_list_1 = int_of_list_1 * 10 + num

        for num in arr_of_list_2:
            int_of_list_2 = int_of_list_2 * 10 + num

        # Remaining operations to get the sum of the numbers
        total_sum_of_linked_lists = int_of_list_1 + int_of_list_2

        reversed_total_sum = str(total_sum_of_linked_lists)[::-1]

        reversed_total_sum_list = [int(digit) for digit in str(reversed_total_sum)]

        head = ListNode(reversed_total_sum_list[0])
        current = head

        for item in reversed_total_sum_list:
            current.next = ListNode(item)
            current = current.next

        return head.next


# Implementing the solution
solution = Solution()

edge_case_1 = ListNode(5, ListNode(6, None))
edge_case_2 = ListNode(5, ListNode(4, ListNode(9, None)))

edge_case_nodes = solution.addTwoNumbers(edge_case_1, edge_case_2)

while edge_case_nodes is not None:
    print(edge_case_nodes.val)
    edge_case_nodes = edge_case_nodes.next
