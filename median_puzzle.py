#There are two sorted arrays nums1 and nums2  with m and n elements respectively. 
#Find the median of the two sorted arrays. The solution should have O(log(m+n)) runtime.

def median(nums1: list, nums2: list) -> int:
    nums1_idx = 0
    nums2_idx = 0
    merged_list = [0] * (len(nums1) + len(nums2))
    while nums1_idx < len(nums1) and nums2_idx < len(nums2):
        if (nums1[nums1_idx] < nums2[nums2_idx]):
            merged_list[nums1_idx + nums2_idx] = nums1[nums1_idx]
            nums1_idx +=1
        else:
            merged_list[nums1_idx + nums2_idx] = nums2[nums2_idx]
            nums2_idx += 1
    print(len(merged_list), merged_list)
    mid = len(merged_list) // 2
    out = merged_list[mid]
    if len(merged_list) % 2 == 0:
        out += merged_list[mid + 1]
        out /= 2
    return  out


def test():
    nums1 = list(range(100))
    nums2 = list(range(25, 120))
    print(median(nums1, nums2))

test()