import java.math.BigInteger;
class Solution {
public int myAtoi(String sl) {
char[] ch = sl.trim().toCharArray();
if(ch.length == 0)
return 0;
String s = "";
if((ch[0] >= '0' && ch[0] <= '9' )|| ch[0] == '-' || ch[0] == '+')
{
if(ch[0] != '+')
s = s + ch[0];
for(int i=1;i<ch.length;i++)
{
if(ch[i] >= '0' && ch[i] <= '9' )
s = s + ch[i];
else
break;
}
}
if(s.isEmpty() || s.equals("-") || s.equals("+"))
return 0;
BigInteger bi = new BigInteger(s);
BigInteger min = new BigInteger(Integer.MIN_VALUE + "");
BigInteger max = new BigInteger(Integer.MAX_VALUE + "");
if(bi.compareTo(min) < 0)
{
return Integer.MIN_VALUE;
}
if(bi.compareTo(max) > 0)
{
return Integer.MAX_VALUE;
}

    return bi.intValue();

}
}