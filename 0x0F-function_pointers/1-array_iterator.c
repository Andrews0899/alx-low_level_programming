#include "function_pointers.h"

/**
 * array_iterator - The object acting as an iterator
 * @array: array to be operated on
 * @size: size of array
 * @action: Action to be performed on the array
 * Return: Nothing
 */
void array_iterator(int *array, size_t size, void (*action)(int))
{
	unsigned int i = 0;

	if (array != NULL && action != NULL && size > 0)
	{
		while (i < size)
		{
			action(array[i]);
			i++;
		}
	}
}
