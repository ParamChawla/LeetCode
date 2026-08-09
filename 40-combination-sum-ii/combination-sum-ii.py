class Solution:

    def backtrack(self, index, nums, total, subset, target, result):

        if total == 0:
            result.append(subset.copy())
            return

        elif total < 0:
            return

        if index >= len(nums):
            return

        for i in range(index, len(nums)):

            if i > index and nums[i] == nums[i-1]:
                continue

            subset.append(nums[i])

            total = total - nums[i]

            self.backtrack(i+1, nums, total, subset, target, result)

            total = total + nums[i]

            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []

        candidates.sort()

        self.backtrack(0, candidates, target, subset, target, result)

        return result