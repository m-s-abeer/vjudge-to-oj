#include <stdio.h>
int main(){
    int i, j=0;
    char ch1[50], ch2[50];
    scanf("%s", ch1);
    scanf("%s", ch2);
    for(i=0; i<48; i++){
        if(ch1[i]>='a' && ch1[i]<=122){
            if(ch1[i]==(ch2[i]+32)) j++;
        }
    }
    if(j>=4) printf("Kafo\n");
    else if(j<=3)printf("Remove\n");
    return 0;
}
