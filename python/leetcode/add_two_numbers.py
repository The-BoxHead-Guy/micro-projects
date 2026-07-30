class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> list[ListNode] | None:

        # Process the Linked List to get the list of nodes extracted
        arr_of_list_1 = []
        arr_of_list_2 = []

        while l1 is not None:
            arr_of_list_1.append(l1.val)
            l1 = l1.next

        while l2 is not None:
            arr_of_list_2.append(l2.val)
            l2 = l2.next

        # Reverse order of the arrays to perform the operation
        arr_of_list_1.reverse()
        arr_of_list_2.reverse()

        # Get the integers of the list
        int_of_list_1 = 0
        int_of_list_2 = 0

        for num in arr_of_list_1:
            int_of_list_1 = int_of_list_1 * 10 + num

        for num in arr_of_list_2:
            int_of_list_2 = int_of_list_2 * 10 + num

        # Remaining operations to get the sum of the numbers
        total_sum_of_linked_lists = int_of_list_1 + int_of_list_2

        reversed_total_sum = int(str(total_sum_of_linked_lists)[::-1])

        reversed_total_sum_list = [int(digit) for digit in str(reversed_total_sum)]

        head = ListNode(reversed_total_sum_list[0])
        current = head

        for item in reversed_total_sum_list:
            current.next = ListNode(item)
            current = current.next

        return head.next


solution_instance = Solution()

# Test case 1
# data_case_1 = [2, 4, 3]
# data_case_2 = [5, 6, 4]

data_case_1 = ListNode(2, ListNode(4, ListNode(3)))
data_case_2 = ListNode(5, ListNode(6, ListNode(4)))

# We first need to create the Linked List, as we only have the solution and ListNode

print(solution_instance.addTwoNumbers(data_case_1, data_case_2))

# Test case 2
data_case_3 = [0]
data_case_4 = [0]

# print(solution_instance.addTwoNumbers(data_case_3, data_case_4))

# Test case 3
data_case_5 = [9, 9, 9, 9, 9, 9, 9]
data_case_6 = [9, 9, 9, 9]

# print(solution_instance.addTwoNumbers(data_case_5, data_case_6))
