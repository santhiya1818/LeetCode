class Solution(object):
    def clumsy(self, n):
        if n <= 0:
            return 0
        st = [n]
        op = 0
        for i in range(n-1,0,-1):
            if op == 0:
                st.append(st.pop() * i)
            elif op == 1:
                st.append(int(float(st.pop()) / i))
            elif op == 2:
                st.append(i)
            elif op == 3:
                st.append(-i)
            op = (op + 1) % 4
        return sum(st)

        