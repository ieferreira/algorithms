#include <iostream>
#include <cstdlib>
#define MAX 100
using namespace std;

int main()
{

    int n;
    int arr[MAX];
    cout << "Enter number: " << endl;
    cin >> n;
    // inputing values in an array

    for (int i = 0; i < n; i++)
    {
        arr[i] = rand();
    }

    // output unsorted

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
    // ascending sorting
    for (int i = 0; i < n; i++)
    {
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[i])
            {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    // display sorted

    cout << "SORTED" << endl;

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    return 0;
}
