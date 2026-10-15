class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups={}
        for word in strs:
            key=tuple(sorted(word))
            groups[key]=groups.get(key,[])+ [word]
        return list(groups.values())


            
   
        