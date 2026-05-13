class Solution:
    def isValid(self, s: str) -> bool:
        # mapping = {'(':')','{':'}','[':']'}
        # temp =[]
        # critic =0
        # for i in range(len(s)):
        #     critic = i #닫힌 기호들의 시작점 인덱스
        #     while s[i] not in (')','}',']'):
        #         temp.append(s[i])
        #         i+=1
        
        # #하나씩 꺼내면서 자기짝꿍이 맞는지 체크하고, 아니면 false 반환
        # for x in range(critic,len(s)):
        #     opened = temp.pop()
        #     if s[x] == mapping[opened]:
        #         continue
        #     else:
        #         return False
        # return True
        mapping = {'}':'{',
                    ')':'(',
                    ']':'['}


        stack =[]

        for st in s:
            if st in '({[':
                stack.append(st)
            else:
                if not stack: #그럼 열린기호가 앞에 하나도 없었다는뜻임
                    return False
                else:
                    opened = stack.pop()
                    if opened != mapping[st]:
                        return False
        return len(stack)==0
        