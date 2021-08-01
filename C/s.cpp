#include <stdio.h>
#include <string>
#include <iostream>
using namespace std;

class Hangman
{
    public:
    char s[128][128] =  {"______","|  |  ","|  0  ","| /|/ ","| / / ","|_____"};
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