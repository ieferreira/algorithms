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

void bubble(int a[], int n)
{
    int i = n - 1;
    while (i > 0)
    {
        if (a[i] < a[i - 1])
        {
            swap(a, i, i - 1);
        }
        i--;
    }
}

void bubbleSort(int a[], int n)
{
    int i = 0;
    while (i < n - 1)
    {
        bubble(a, n);
        i++;
    }
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

    display(arr, n);
    bubbleSort(arr, n);
    display(arr, n);
}