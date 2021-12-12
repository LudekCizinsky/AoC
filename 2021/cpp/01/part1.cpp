#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream f;

    f.open("1.in");
    if (!f)
    {
        cout << "Unable to open file";
        exit(1); // terminate with error
    }

    int prev = 0;
    int curr = 0;
    int i = 0;
    int c = 0;

    while (f >> curr)
    {
        if (i != 0 && curr > prev)
        {
            c += 1;
        }

        prev = curr;
        i += 1;
    }

    f.close();
    cout << to_string(c);
    return 0;
}