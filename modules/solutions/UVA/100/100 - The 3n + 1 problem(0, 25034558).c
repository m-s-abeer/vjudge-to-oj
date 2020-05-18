#include<stdio.h>
int main()
{
    long x,y,i,j,k,counter,max;
    while(scanf("%ld %ld",&x,&y)==2)
    {
        printf("%ld %ld ",x,y);
        if(x>y) x=x+y-(y=x);
        max=1;
        for(i=x;i<=y;i++)
        {
            k=i;
            counter=1;
            while(k!=1)
            {
                if(k%2==0)
                    k/=2;
                else
                    k=3*k+1;
                counter++;
            }
            if(counter>max) max=counter;
        }
        printf("%ld\n",max);
    }
    return 0;
}
