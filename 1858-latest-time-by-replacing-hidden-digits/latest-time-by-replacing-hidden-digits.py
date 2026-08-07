class Solution:
    def maximumTime(self, time: str) -> str:
        x = list(time)

        if x[0] == '?':
            if x[1] == '?' or x[1] in "0123":
                x[0] = '2'
            else:
                x[0] = '1'

        if x[1] == '?':
            if x[0] == '2':
                x[1] = '3'
            else:
                x[1] = '9'

        if x[3] == '?':
            x[3] = '5'

        if x[4] == '?':
            x[4] = '9'

        return "".join(x)