class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strss=[]
        for i in strs:
            k=list(i)
            k.sort()
            m="".join(k)
            strss.append(m)
        l=[]
        seen=set()
        for i in range(len(strss)):
            l1=[]
            if i in seen:
                continue
            for j in range(i,len(strss)):
                if strss[i]==strss[j]:
                    l1.append(strs[j])
                    seen.add(j)
            l.append(l1)
        return l