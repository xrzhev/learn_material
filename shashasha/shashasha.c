#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>


void init_seq(int argc, char **argv, unsigned char sha1s[8][64]) {
    if ( argc != 2 ) {
        puts("FAILED: ARGUMENT ERROR");
        exit(0);
    }
    if ( 32 != strlen(argv[1]) ) {
        puts("FAILED: FLAG LENGTH ERROR");
        exit(0);
    }
}


char *sha1_2_hex(const unsigned char *sha1)
{
    static int bufno;
    static char hexbuffer[4][50];
    static const char hex[] = "0123456789abcdef";
    char *buffer = hexbuffer[3 & ++bufno], *buf = buffer;

    for (int i = 0; i < 20; i++) {
        unsigned int val = *sha1++;
        *buf++ = hex[val >> 4];
        *buf++ = hex[val & 0xf];
    }
    *buf = '\0';

    return buffer;
}



int main(int argc, char **argv) {
    int success_count = 0;
    unsigned char sha1s[8][64] = { {"0a6eb6a849b63d4fa63e29f7ceab89726f705769"},
                                   {"3202af96d27db6239c1410ff9c90e1048836c409"},
                                   {"c3d237710219ed312f7279a0e0f5c028c1a5d284"},
                                   {"f3abcb4771fbbb6764ab1d4db6b2cf0629afd04b"},
                                   {"4a691dd824f3a3d60a006324c0ded7dfad54322f"},
                                   {"6a72c7d99255166be8f9af622bacbaa14c2c39ae"},
                                   {"fc5052fec0e53e73a8e397c1270f27dc7b43f262"},
                                   {"1528e3b012954182470c824df10ee1e379f1f32c"} };
  
  
    init_seq(argc, argv, sha1s);

    for (int i = 0; i < 8; i++) {
      unsigned char hash_digest[SHA_DIGEST_LENGTH];
      unsigned char cur_user_word[5];
      
      //argvから4文字切り出し
      strncpy(cur_user_word, argv[1]+(i*4), 4);
      cur_user_word[4] = '\0';

      //SHA1ハッシュ作成
      SHA1(cur_user_word, strlen(cur_user_word), hash_digest);
      if (strcmp(sha1s[i], sha1_2_hex(hash_digest)) == 0) {
          success_count++;
      }

      printf("TARGET SHA1[%d]: %s  [????]\n", i, sha1s[i]);
      printf("INPUT  SHA1[%d]: %s  [%s]\n", i,sha1_2_hex(hash_digest), cur_user_word);
      puts("---------------------------------------------------");
    }

    if (success_count == 8) {
      puts("YOU WIN!");
    }
  
  return 0;
}
