#include <stdio.h>



void drawboard(){

    printf("%c | %c | %c ", coords[0], coords[1], coords[2]);
    printf("- - - - - - -\n");
    printf("%c | %c | %c\n", coords[3], coords[4], coords[5]);
    printf("- - - - - - -\n");
    printf("%c | %c | %c\n", coords[6], coords[7], coords[8]);





}

int main(){

    // 0 is false, these are booleans
    int computerwin = 0;
    int playerwin = 0; 
    int move;
    char *coords[9] = {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL};
    printf("Enter the coordinate you would like to move to:\n");
    scanf('%d' &move);
    return 0; 

}