class solution{
    public int  tri(int r,int c){
        if(c==0){
            return 1;
        }if(r==c){
            return 1;
        }
        return tri(r-1,c)+tri(r-1,c-1);

    }
    public static void main(String [] args){
        solution s=new solution();
        System.out.println(s.tri(1,0));
    }
}