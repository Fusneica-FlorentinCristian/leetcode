class Solution:
    def mapToDict(self, s:str) -> dict:
        mydict = {}
        for x in s:
            if x in mydict:
                mydict[x] += 1
            else:
                mydict[x] = 1
        return mydict
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = self.mapToDict(s)
        dictt = self.mapToDict(t)
        return dicts == dictt