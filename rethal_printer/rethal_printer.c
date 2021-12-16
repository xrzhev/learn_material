#include <stdio.h>
#include <stdlib.h>

void initialize(void) {
    alarm(60);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void) {
    FILE *fp = NULL;
    char flag[64];
    char buf[64];

    initialize();
    fp = fopen("./flag.txt", "r");
    if (fp == NULL) {
        printf("Nothing Flag! exit...\n");
        exit(0);
    }
    fscanf(fp, "%s", flag);
    fclose(fp);

    fgets(buf, sizeof(buf), stdin);
    printf(buf);
    if (buf == flag) {
        printf("%s", flag);
    } else {
        printf("Wrong!\n");
    }
}
