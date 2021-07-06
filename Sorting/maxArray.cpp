#include "iostream"

using namespace std;

int main(int argc, char)
{
    int sum = 0;
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int size = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < size; i++)
    {
        sum += arr[i];
    }
    cout << sum << endl;
    return 0;
}