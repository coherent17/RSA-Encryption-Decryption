#include <stdio.h>

int main(){

    int r, e;
    printf("please enter your public key (r, e)\n");
    scanf("%d %d", &r, &e);
    for (int i = 0; i < 100;i++){
        if((((r * i)+1)%e)==0){
            printf("d= %d , k= %d\n", (int)(1+i*r)/e, i);
        }
    }
    return 0;
}