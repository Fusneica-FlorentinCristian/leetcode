class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_num = 0
        copy_x = x
        while x > 0:
            new_num = new_num * 10 + x % 10
            x = int(x / 10)
        return new_num == copy_x