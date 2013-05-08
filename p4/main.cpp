#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <iterator>
using namespace std;

int main()
{
    ifstream myFile ("integers", ios::in | ios::binary);

    int i, max_i, current; // = 2147383590;

    set<int> numbers;
    set<int> missingNumbers;
    set<int>::const_iterator it1, itEnd;

    // First interval, from 0 to 99950
    i = 0;
    max_i = 99950;
    
    myFile.seekg(i * sizeof(int));
    while (i != max_i) 
    {
        myFile.read((char*)&current, sizeof(int));        
        numbers.insert(current);
        i++;
    }

    // Third interval, from 2147383597 to end
    i = 2147383597;
    max_i = 2147483548;

    myFile.seekg(i * sizeof(int));
    while (i != max_i) 
    {
        myFile.read((char*)&current, sizeof(int));        
        numbers.insert(current);
        i++;
    }

    /*
    // Second interval, consecutive numbers from 100000 to 2147383647
    max_i = 2147383597;
    i = 99950;

    myFile.seekg(i * sizeof(int));
    while (i != max_i) 
    {
        myFile.read((char*)&current, sizeof(int));        
        cout << i << " - " << current << endl;

        i++;
    }
    //*/

    i = 0;
    for(it1 = numbers.begin(), itEnd = numbers.end(); it1 != itEnd; ++it1)
    {
        while (i < *it1) 
        {
            missingNumbers.insert(i);
            i++;
        }
        i = *it1 + 1;

        if (i == 100000) {
            i = 2147383647;
        }
    }
    //*/


    myFile.close();    


    int numCases, currentCase;
    cin >> numCases;

    for (int i = 0; i < numCases; ++i)
    {
        cin >> currentCase;
        it1 = missingNumbers.begin();
        advance(it1, currentCase - 1);

        cout << *it1 << endl;
    }



    return 0;
}
