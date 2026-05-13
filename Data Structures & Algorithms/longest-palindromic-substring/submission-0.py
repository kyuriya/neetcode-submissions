class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i:j+1]

                if temp == temp[::-1]:
                    if len(temp) > len(answer): #지금 찾은 팔린드롬이 기존 순회에서의 팔린드롬보다 길면 답이디
                        answer = temp

        return answer