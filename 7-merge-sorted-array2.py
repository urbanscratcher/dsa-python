"""
<정렬된 배열의 정합2>
정렬된 배열 nums1과 nums2가 주어지고, 각 크기는 m과 n. 정렬을 유지하면서 nums1 배열부터 채워나가 nums2까지 확장하기

* 6의 nums1처럼 병합된 m+n 크기의 공간은 없음
* nums1 배열에 nums1과 nums2의 모든 요소를 작은 수부터 채워나가고, nums2에는 나머지를 정렬을 유지하며 넣도록 하자
* 추가 배열 할당 없이 문제를 해결해야 함 (공간 복잡도 O(1))

- geeksforgeeks: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1

예
nums1=[1,3,5,7]
nums2=[2,4,8]
최종적으로
nums1=[1,2,3,4]
nums2=[5,7,8]

제한사항
1. 추가 배열 공간 할당이 없다
2. nums1과 nums2의 크기는 제한이 없음
3. nums1과 nums2의 요소는 정렬돼 있음

아이디어1 - Brute-force
1. nums1을 순회
2. nums1 요소와 nums2 첫 요소와 크기 비교
3. nums1 요소가 nums2 첫 요소보다 크면
  - nums2의 첫 요소를 nums1의 비교했던 요소와 교체, 변경된 nums2의 첫 요소와 다른 요소를 비교하며 정렬
4. 두 배열이 계속 정렬된 채로 nums1의 순회가 끝날 때까지 비교 및 교환을 진행
시간 복잡도: O(mn)
공간 복잡도: O(1)

아이디어2 - two pointers
TBD

아이디어3 - gap method (shell sort)
TBD

"""


def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    for i, v in enumerate(nums1):
        if v > nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = v

            # 재정렬
            k = 0
            for j, w in enumerate(nums2[1:], start=1):
                if (nums2[0] >= nums2[j]):
                    k = j
                else:
                    break

            if k > 0:
                for k, x in enumerate(nums2[1:k+1], start=1):
                    nums2[k-1] = nums2[k]
                nums2[k] = v


nums1 = [1, 3, 5, 7]
m = 4
nums2 = [0, 2, 6, 8, 9]
n = 5
merge(nums1, m, nums2, n)
print(f'nums1: {nums1}\nnums2: {nums2}')
