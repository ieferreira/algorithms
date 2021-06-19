#include <iostream>
#include <cstdlib>
#define MAX 100
using namespace std;

void swap(int a[], int x, int y)
{
    int temp = a[x];
    a[x] = a[y];
    a[y] = temp;
}

int locOfSmallest(int a[], int s, int e)
{
    // loops trying to find the smallest
    int i = s;
    int j = i;
    while (i <= e)
    {
        if (a[i] < a[j])
        {
            j = i;
        }
        i++;
    }
    return j;
}

void display(int a[], int n)
{
    int i = 0;
    while (i < n)
    {
        cout << a[i] << ", ";
        i++;
    }
    cout << endl;
}

void selectionSort(int a[], int n)
{
    int i = 0;
    while (i < n - 1)
    {
        int j = locOfSmallest(a, i, n - 1);
        swap(a, i, j);
        i++;
    }
}

int main()
{

    int n;
    int arr[MAX];
    cout << "Enter number: " << endl;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        arr[i] = rand();
    }

    // calculate size of array if not given
    // int size = sizeof(arr)/sizeof(int);
    // inputing values in an array
    cout << "RANDOM ARRAY GENERATED" << endl;
    display(arr, n);
    selectionSort(arr, n);
    cout << "RANDOM ARRAY SORTED" << endl;
    display(arr, n);

    return 0;
}
