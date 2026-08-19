from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(l, r):
            if l >= r:
                return

            mid = (l + r) // 2

            merge_sort(l, mid)
            merge_sort(mid + 1, r)

            merge(l, mid, r)

        def merge(l, mid, r):
            temp = []
            i = l
            j = mid + 1

            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            while i <= mid:
                temp.append(nums[i])
                i += 1

            while j <= r:
                temp.append(nums[j])
                j += 1

            for w in range(len(temp)):
                nums[l + w] = temp[w]

        merge_sort(0, len(nums) - 1)
        return nums