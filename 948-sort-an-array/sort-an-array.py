class Solution(object):
    def mergeSort(self, arr, s, e):
        if s >= e:
            return
        
        mid = (s + e) // 2
        self.mergeSort(arr, s, mid)
        self.mergeSort(arr, mid + 1, e)
        self.merge(arr, s, e, mid)

    def merge(self, arr, s, e, mid):
        L = arr[s: mid + 1]
        R = arr[mid + 1: e + 1]

        i, j, k = 0, 0, s

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def sortArray(self, nums):
        if not nums or len(nums) == 1:
            return nums
        
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

     