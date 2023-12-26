"""
<정렬된 배열에서 중복 제거>
정렬된 배열의 요소들을 중복 없이 단 1번씩만 가질 수 있도록 주어진 배열을 그대로(in-place) 수정하고, 수정된 배열의 새로운 길이를 반환하라

* 추가적인 배열의 할당은 하지 않고, 중복 요소를 하나만 남기고 걸러내는 함수를 만드는 것이다. 반환된 길이 이후에 있는 데이터는 무시해도 된다.

입력값: nums = [0, 0, 0, 1, 2, 2, 2]

- leetcode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/


제한사항
1. 정수형 배열
2. 입력으로 주어지는 배열이 0일 수 있다
3. 추가 배열 할당 없이 입력 배열을 그대로 수정할 것
4. 반환값은 정수, 배열 길이보다 작거나 같음

아이디어 - 모든 경우의 수(Brute-force)
1. 맨 첫 요소(curr)를 저장
2. 맨 첫 요소를 제외하고 순회
  - 1 ~ n-1 순회, count 초기값은 1
  - curr와 값이 같다면 다음 요소로 넘어감
  - curr과 값이 같지 않다면, curr을 현재 값으로 업데이트하고 count++
  - count 값을 증가시키기 전에 count가 인덱스가 되어 해당 공간에 달라진 curr 값으로 업데이트
시간 복잡도 : O(n)
공간 복잡도 : O(1)

"""


def removeDuplicates(nums: list[int]) -> int:
    if len(nums) <= 0:
        return 0
    curr = nums[0]
    cnt = 1
    for i in range(1, len(nums)):
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr
            cnt += 1
    return cnt


# 테스트
nums = [0, 0, 0, 1, 2, 2, 2]
print(removeDuplicates(nums))
