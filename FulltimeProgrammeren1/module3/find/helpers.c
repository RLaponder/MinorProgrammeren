/****************************************************************************
 * helpers.c
 *
 * Fulltime Programmeren 1
 * Robin Laponder
 *
 * Sorts an array of values and searches for a specific value.
 ***************************************************************************/

#include <cs50.h>

#include "helpers.h"

#include <stdio.h>

// Returns true if value is in array of n values, else false
bool search(int value, int values[], int n)
{
    // return false if entered value is non-positive
    if (value < 0)
    {
        return false;
    }

    // set left and right for the whole array
    int left = 0, right = n - 1;

    // search through the array as long as there are elements in the array
    while (n > 0)
    {
        // set the middle of the array
        int middle = (right - left) / 2 + left;

        // return true when the middle value is the needle
        if (values[middle] == value)
        {
            return true;
        }

        // search right half of the array
        else if (values[middle] < value)
        {
            left = middle + 1;
        }

        // search left half of the array
        else if (values[middle] > value)
        {
            right = middle - 1;
        }

        // set new number of values in the unsearched part of the array
        n = right - left + 1;
    }

    // the value is not in the array, so return false
    return false;
}

// Sorts array of n values
void sort(int values[], int n)
{
    // iterate over the values in the array
    for (int i = 0; i < n - 1; i++)
    {
        // set minimum of the array
        int minimum = i;

        // iterate over array to find the lowest integer
        for (int j = i; j < n; j++)
        {
            // replace minimum by the lowest integer
            if (values[j] < values[minimum])
            {
                minimum = j;
            }
        }

        // check if the minimum changed and swap values if it did
        if (i != minimum)
        {
            int temp_i = values[minimum];
            values[minimum] = values[i];
            values[i] = temp_i;
        }
    }
    return;
}