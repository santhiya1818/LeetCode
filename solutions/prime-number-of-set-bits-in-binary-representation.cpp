class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        const int range = 20;
        bitset<range> bt;
        bt.set(2);
        for(int i = 3; i < range; i += 2)
        {
            bt.set(i);
        }
        for(int i = 3; i * i < range; i += 2)
        {
            if(bt[i])
            {
                for(int j = i; j * i < range; j += 2)
                {
                    bt.reset(j * i);
                }
            }
        }
        int res = 0;
        for(int i = left; i <= right; i++)
        {
            int count = 0;
            int temp = i;
            while(temp)
            {
                count++;
                temp &= (temp - 1);
            }
            if(bt[count])
            {
                res++;
            }
        }
        return res;
    }
};