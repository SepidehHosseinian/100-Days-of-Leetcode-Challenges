class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        res = int('-' + s[1:][::-1]) if s[0] == '-' else int(s[::-1])
        return res if -2147483648 <= res <= 2147483647 else 0