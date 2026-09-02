class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r,l = 0, len(numbers)-1
        while r < l:
            total = numbers[r] + numbers[l]
            if total > target:
                l -= 1
            elif total < target:
                r += 1
            else:
                return [r+1,l+1]