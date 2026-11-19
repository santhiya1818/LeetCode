class Solution {
public:
    int binaryGap(int n) {
        string binary="";

        while(n>0){
            binary = (n%2==0?'0':'1')+binary;
            n /=2;
        }

        int mg =0,lastidx = -1;


        for(int i=0;i<binary.size();i++){
            if(binary[i]=='1'){
                if(lastidx != -1){

                    mg = max(mg,i-lastidx);
                }
                lastidx=i;
            }

        }
        return mg;
        
    }
};