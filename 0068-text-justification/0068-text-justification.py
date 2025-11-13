class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        curr = []
        num_of_letters = 0
        
        for w in words:
            
            if num_of_letters + len(w) + len(curr) > maxWidth:
                spaces = maxWidth - num_of_letters
                gaps = len(curr) - 1

                if gaps == 0:
                    line = curr[0] + ' ' * spaces
                else:
                    space_each = spaces // gaps
                    extra = spaces % gaps
                    line = ''
                    for i in range(gaps):
                        line += curr[i]
                        line += ' ' * (space_each + (1 if i < extra else 0))
                    line += curr[-1]
                res.append(line)

                # reset for next line
                curr = []
                num_of_letters = 0

            curr.append(w)
            num_of_letters += len(w)

        last_line = ' '.join(curr)
        last_line += ' ' * (maxWidth - len(last_line))
        res.append(last_line)

        return res