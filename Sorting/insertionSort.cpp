#include <iostream>
#include <cstdlib>
#define MAX 100
using namespace std;

void insertIth(int a[], int n, int i)
{
    int key = a[i];
    int j = i - 1;
    while (j >= 0 && a[j] > key)
    {
        a[j + 1] = a[j];
        j = j - 1;
    }
    a[j + 1] = key;
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

void insertionSort(int a[], int n)
{

    int i = 1;
    while (i < n)
    {
        insertIth(a, n, i);
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

    display(arr, n);
    insertionSort(arr, n);
    display(arr, n);
}