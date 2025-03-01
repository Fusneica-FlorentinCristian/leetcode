class Solution:
    def mapToDict(self, s:str) -> dict:
        mydict = {}
        for x in s:
            if x in mydict:
                mydict[x] += 1
            else:
                mydict[x] = 1
        return mydict
    def removeFromDict(self, t:str, mydict:dict) -> bool:
        for x in t:
            if x not in mydict:
                return False
            else:
                mydict[x] -= 1
                if mydict[x] < 0:
                    return False

        for i in mydict:
            if mydict[i] != 0:
                return False
        return True
    def isAnagram(self, s: str, t: str) -> bool:
        return self.removeFromDict(t, self.mapToDict(s))