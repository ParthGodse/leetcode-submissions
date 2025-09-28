class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # bulls = 0
        # unmatched_secret = []
        # unmatched_guess = []
        # for i, j in zip(secret, guess):
        #     if i == j:
        #         bulls += 1
        #     else:
        #         unmatched_secret.append(i)
        #         unmatched_guess.append(j)

        # counter_secret = Counter(unmatched_secret) 
        # counter_guess = Counter(unmatched_guess)
        # cows = sum((counter_secret & counter_guess).values())
        cows = 0
        match_ind = [i for i in range(min(len(secret),len(guess))) if secret[i] == guess[i]]
        count = len(match_ind)
        for c in set(secret):
            cows += min(secret.count(c), guess.count(c))
        return f"{count}A{cows-count}B"
