class Solution: 
    def permute(self, nums: List[int]) -> List[List[int]]:  
        result = [[]]  # 처음에는 빈 순열 하나에서 시작

        for num in nums:  # nums의 숫자를 하나씩 꺼내서 기존 순열들에 끼워 넣을 것
            new_result = []  # 이번 num을 끼워 넣어서 새로 만들 순열들을 저장할 리스트

            for arr in result:  # 지금까지 만들어진 순열 하나씩 꺼내기
                for i in range(len(arr) + 1):  # arr의 모든 삽입 위치를 순회, 맨 앞부터 맨 뒤까지
                    temp = arr[:i] + [num] + arr[i:]  # arr의 i번째 위치에 num을 끼워 넣은 새 리스트 생성
                    new_result.append(temp)  # 새로 만든 순열을 new_result에 추가

            result = new_result  # 이번 num까지 반영된 순열 목록으로 result 갱신

        return result  # 모든 숫자를 반영한 최종 순열 리스트 반환