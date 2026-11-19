class Solution {
public int reverse(int x) {

    int answer = 0;
    
    
    while(x!=0){
        int digit = x%10;
        

        if((answer > 2147483647/10) || (answer < -2147483647/10)){
            return 0;
        }
        answer = (answer * 10) + digit;
        x = x/10;

    }
    return answer;
    
}
}