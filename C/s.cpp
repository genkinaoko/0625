#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

class Hangman
{
    public:
    /*char s[6][15]={"______","|  |  ","|  0  ","| /|/ ","| / / ","|_____"};*/
    char d[4][4] = {"www","rrr","qqq"};
    void Show();
};

void Hangman::Show()
{
    for(int i = 0; i < 3; i++)
    {
        printf("%s\n",d[i]);
    }
}

int main()
{
    Hangman h;
    h.Show();
}