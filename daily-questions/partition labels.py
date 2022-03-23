class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        di = {}
        for i in range(len(s)):
            if s[i] not in di:
                di[s[i]] = [i,i]
            else:
                di[s[i]][1] = i
        st = en = 0
        bound = di[s[0]][1]
        ans = []
        while en < len(s):
            if en > bound:
                ans.append(en - st)
                st = en
                bound = di[s[st]][1]
                en += 1
                continue
            if di[s[en]][1] > bound:
                bound = di[s[en]][1]
                en += 1
            else:
                en += 1
        ans.append(en - st)   
        return ans
                
                