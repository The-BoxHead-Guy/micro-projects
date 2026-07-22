class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for outer_index, outer_num in enumerate(nums):
            for inner_index, inner_num in enumerate(nums):
                if inner_index == outer_index:
                    continue

                if (inner_num + outer_num) == target:
                    return [outer_index, inner_index]

        return []


# Test cases

solution = Solution()
# print(class_instance.print_test())

# Test case 1
test_nums_1 = [2, 7, 11, 15]
test_target_1 = 9

print(solution.twoSum(test_nums_1, test_target_1))

# Test case 2
test_nums_2 = [3, 2, 4]
test_target_2 = 6

print(solution.twoSum(test_nums_2, test_target_2))

# Test case 3
test_nums_3 = [3, 3]
test_target_3 = 6

print(solution.twoSum(test_nums_3, test_target_3))

# Test case 3
test_nums_4 = [10, 4, 3, 15, 6]
test_target_4 = 9

print(solution.twoSum(test_nums_4, test_target_4))
