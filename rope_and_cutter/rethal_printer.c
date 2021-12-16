#include <stdio.h>
#include <stdlib.h>


char args[32] = "/bin/cat ./flag.txt";

void initialize(void) {
    alarm(60);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main(void) {
    char buf[32];

    initialize();
    gets(buf, stdin);
    system("/bin/echo 'Hello, world!'");
}
