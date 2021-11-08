#include <stdio.h>

int quick(int a,int b,int c){
    int ans=1;
    a=a%c;
    while(b!=0){
        if(b&1) ans=(ans*a)%c;
        b>>=1;
        a=(a*a)%c;
    }
return ans;
}

int main(){
    while(1){
        printf("calculate (a^b)mod c\n");
        printf("please enter a, b, c:\n");
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        int answer = quick(a, b, c);
        printf("answer = %d\n", answer);
    }
    return 0;
}