class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        welth = []
        for i in range(len(accounts)):
            welth.append(sum(accounts[i]))
        
        richest = max(welth)
        return richest
        



        