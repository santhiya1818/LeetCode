class Solution(object):
    def angleClock(self, hour, minutes):
        m = minutes * 6
        h = (hour%12) * 30 + minutes * 0.5
        dif = abs(h-m)
        return min(dif , 360 - dif)
        