class Solution(object):
    def judgeCircle(self, moves):
        if moves.count("U") != moves.count("D"):
            return False
        if moves.count("L") != moves.count("R"):
            return False
        if moves.count("U") != moves.count("D") and moves.count("L") != moves.count("R"):
            return False
        else:
            return True
        