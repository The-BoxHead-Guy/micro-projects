class Solution:
    def print_test(self):
        print("This is a test because I don't know how to use classes in python wtf")

    def sum_two_numbers(self, first, second) -> int:
        return first + second

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        found_indexes: list[int] = []

        for outer_index, outer_num in enumerate(nums):
            for inner_index, inner_num in enumerate(nums):
                if inner_index == outer_index:
                    continue

                inner_sum = self.sum_two_numbers(inner_num, outer_num)

                if inner_sum == target:
                    found_indexes.append(outer_index)
                    found_indexes.append(inner_index)

                    break

            if found_indexes:
                break

        print(found_indexes)

        return found_indexes


# Test cases

solution = Solution()
# print(class_instance.print_test())

# Test case 1
test_nums_1 = [2, 7, 11, 15]
test_target_1 = 9

solution.twoSum(test_nums_1, test_target_1)

# Test case 2
test_nums_2 = [3, 2, 4]
test_target_2 = 6

solution.twoSum(test_nums_2, test_target_2)

# Test case 3
test_nums_3 = [3, 3]
test_target_3 = 6

solution.twoSum(test_nums_3, test_target_3)
