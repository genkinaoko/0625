#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

class Hangman
{
    public:
<<<<<<< HEAD
    char s[128][128] =  {"______","|  |  ","|  0  ","| /|/ ","| / / ","|_____"};
=======
    char s[6][15]={"______","|  |  ","|  0  ","| /|/ ","| / / ","|_____"};
    char d[4][4] = {"www","rrr","qqq"};
>>>>>>> f9cd6371f21011c8de7193af6633be4f9412e530
    void Show();
};

void Hangman::Show()
{
    for(int i = 0; i < 6; i++)
    {
        printf("%s\n",s[i]);
    }
}

int main()
{
    Hangman h;
    h.Show();
}