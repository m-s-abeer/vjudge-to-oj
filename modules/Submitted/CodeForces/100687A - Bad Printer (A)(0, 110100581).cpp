#include <stdio.h>
int main(){
    int i, j, m=0;
    char ch[15];
    gets(ch);
    for(i=0; i<8; i++){
        if(ch[i]=='?') m++;
    }
    if(m>0) printf("No\n");
    else printf("Yes\n");
    return 0;
}
