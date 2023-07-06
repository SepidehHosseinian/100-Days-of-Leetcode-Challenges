class Solution:
    def defangIPaddr(self, address: str) -> str:
        if "." in address:
            n_address = address.replace(".", "[.]")
        return n_address