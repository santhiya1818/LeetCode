class Solution {
public void backTrack(List res ,String s, int n , int left , int right){
if(s.length() == 2 * n){
res.add(s);
return ;
}
if (left < n)
backTrack(res , s + '(' , n , left + 1 , right);
if (right < left)
backTrack(res , s + ')' , n , left , right + 1);

}
public List<String> generateParenthesis(int n) {
    List<String> ans = new ArrayList<>();
    backTrack(ans , "" , n , 0 , 0);
    return ans;
}

}