#include <algorithm>
#include <iostream>
#include <string>
#include <fstream>

#define ZN 256

using namespace std;

void przygotujZleZnaki(const string &wzor, int dl, int tabela[ZN])
{
    for (int i = 0; i < ZN; i++)
        tabela[i] = -1;

    for (int i = 0; i < dl; i++)
        tabela[(unsigned char)wzor[i]] = i;
}

void znajdz(const string &tekst, const string &wzor)
{
    int dlW = wzor.size();
    int dlT = tekst.size();

    int tabZlych[ZN];
    przygotujZleZnaki(wzor, dlW, tabZlych);

    int przes = 0;

    while (przes <= dlT - dlW)
    {
        int idx = dlW - 1;

        while (idx >= 0 && wzor[idx] == tekst[przes + idx])
            idx--;

        if (idx < 0)
        {
            cout << "Znaleziono na indeksie = " << przes << endl;

            if (przes + dlW < dlT)
                przes += dlW - tabZlych[(unsigned char)tekst[przes + dlW]];
            else
                przes++;
        }
        else
        {
            przes += max(1, idx - tabZlych[(unsigned char)tekst[przes + idx]]);
        }
    }
}

int main()
{
    ifstream plik("text.txt");
    if (!plik.is_open())
    {
        cerr << "Nie mozna otworzyc pliku text.txt!" << endl;
        return 1;
    }

    string tekst(
        (istreambuf_iterator<char>(plik)),
        istreambuf_iterator<char>()
    );

    plik.close();

    string wzor = "kota";

    znajdz(tekst, wzor);

    return 0;
}