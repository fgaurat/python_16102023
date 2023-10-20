#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include"hello.h"

void sayHello(void){
    printf("sayHello\n");
}

void hello(const char* name){
    printf("Hello %s\n",name);
}

int randNum(void){
    srand(time(NULL));
    int nRand = rand()%50;
    return nRand;
}