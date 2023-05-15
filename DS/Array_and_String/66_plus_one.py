class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        sums = digits[-1] + 1
        carry = 1 if sums > 9 else 0  
        digits[-1] = 0 if sums > 9 else sums

        for i in range(len(digits)-2, -1, -1):
            if digits[i] + carry > 9:
                carry = 1
                digits[i] = 0
            else:
                digits[i] = digits[i] + carry
                carry = 0
        
        if carry == 1:
            digits.append(1)
            return digits[::-1]

        return digits
    
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num=int(''.join(str(e)for e in digits))+1
        res = map(int,str(num))
        return res        