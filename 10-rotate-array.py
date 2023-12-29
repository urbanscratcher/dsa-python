"""
<배열의 회전>
입력으로 정수형 배열과 k값이 주어지면, 각 요소를 우측으로 k번 이동 및 회전 해보자. k는 양의 정수 값. nums 배열에 [1,2,3,4]가 있고, k가 1이라면 요소는 우측으로 1칸씩 이동 및 회전해 [4,1,2,3]이 됨

- leetcode: https://leetcode.com/problems/rotate-array

제한사항
1. 정수형 배열
2. k값은 양의 정수

아이디어1 - brute-force
1. k번만큼 순회
2. 배열 요소를 1칸씩 우측으로 이동 및 회전시킴
시간 복잡도: O(n*k)
공간 복잡도: O(1)


아이디어2 - 임시배열
1. 입력과 같은 크기의 임시 배열(temp) 생성
2. nums 배열 순회
  - temp 배열에 nums 요소를 k만큼 이동 및 회전시킨 위치에 값 삽입
3. 임시 배열 순회
  - temp 배열 요소를 nums 배열에 같은 인덱스 값을 복사
시간 복잡도: O(n)
공간 복잡도: O(n)


아이디어3 - 교환
1. 모든 요소가 한 번씩 교환될 때까지 배열 순회
2. 요소를 k만큼 이동 및 저장
  - 이동한 위치의 이전 요소는 저장
  - 저장한 요소는 다음 k만큼 이동하여 넣음
  - 시작한 요소까지 값을 이동시키면 해당 순회 종료
  - 이동시킬 때마다 카운트 
  - 다음 요소를 선택하고 다시 2번 내용 반복
시간 복잡도: O(n)
공간 복잡도: O(1)

아이디어4 - 3번 뒤집기 (수학적)
1. 전체 숫자 뒤집기
2. 처음 k만큼까지 숫자 뒤집기
3. 이전에 뒤집은 숫자 다음(n-k)부터 마지막(n)까지 뒤집기
시작 복잡도: O(n)
공간 복잡도: O(1)




"""


def rotate1(nums: list[int], k: int) -> None:
    length = len(nums)
    for _ in range(k):
        prevNum = nums[length-1]
        for i in range(length):
            temp = nums[i]
            nums[i] = prevNum
            prevNum = temp


nums = [1, 2, 3, 4]
rotate1(nums, 2)
print(nums)


def rotate2(nums: list[int], k: int) -> None:
    length = len(nums)
    tempArr = [0]*len(nums)

    for i, v in enumerate(nums):
        newIndex = (i+k) % length
        tempArr[newIndex] = nums[i]
    nums[:] = tempArr


nums = [1, 2, 3, 4]
rotate2(nums, 2)
print(nums)


def rotate3(nums: list[int], k: int) -> None:
    length = len(nums)
    count = 0

    for start in range(length):
      # 파이썬은 for 루프 종료 조건을 if-break 형태로 따로 정의해야 함
        if count >= length:
            break
        currIdx = start
        prev = nums[start]

      # 파이썬에서 do-while 사용하려면 하단과 같이 해야 함
        while True:
            nextIdx = (currIdx + k) % length
            temp = nums[nextIdx]
            nums[nextIdx] = prev
            prev = temp

            currIdx = nextIdx
            count += 1

            if currIdx == start:
                break


nums = [1, 2, 3, 4]
rotate3(nums, 2)
print(nums)


def rotate4(nums: list[int], k: int) -> None:
    length = len(nums)
    k = k % length
    nums[:] = nums[::-1]
    nums[0:k] = nums[0:k][::-1]
    nums[k:length] = nums[k:length][::-1]


nums = [1, 2, 3, 4]
rotate4(nums, 2)
print(nums)
