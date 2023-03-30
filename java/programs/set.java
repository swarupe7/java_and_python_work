import java.util.*;
class solution{
    public static void main(String[]args){
        LinkedHashSet<Integer> hs=new LinkedHashSet<>();
        hs.add(5);
        hs.add(7);
        hs.add(-1);
        for(Integer i:hs){
            System.out.println(i);
        }
    }
}