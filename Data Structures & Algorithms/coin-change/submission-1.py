class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # recurrance relation: 
        # Cost(amount) = 1 + min{Cost(amount - c1), ..., Cost(amount-cn)}
        # coins = [c1, ..., cn]
        # Memoization (Top Down Approach):
        def coinMemo(coins: list[int], amount: int, memo: dict[int]) -> int:
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            new_coins = float('inf')
            for c in coins:
                if amount - c >= 0:
                    new_coins = min(new_coins, 1 + coinMemo(coins, amount - c, memo))
            
            memo[amount] = new_coins
            return memo[amount]
        
        memo = {}
        res = coinMemo(coins, amount, memo)
        if res == float('inf'):
            return -1
        return res

        # coins = [1, 5, 10]
        # amount = 12
        # coinMemo(12) = 1 + min(2, 3, 2) = 3

        # memo = {10: 1, 5: 1, 1: 1, 6: 2, 11: 2, 2: 2, 7: 3}
        # coinMemo(11) = 2
            # coinMemo(10) = 1
            # coinMemo(6) = 2
            #   coinMemo(5) = 1
            #   coinMemo(1) = 1
            # coinMemo(1) = 1

        # coinMemo(7) = 3
            # coinMemo(6) = 2
            # coinMemo(2) = 2
                # coinMemo(1) = 1
        
        # coinMemo(2) = 2

        

