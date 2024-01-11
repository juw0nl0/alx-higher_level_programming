#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - prints all elements of a dlistint_t list.
 * @h: head of a doubly linked list
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t num = 0;

	while (ptr && ptr -> prev)
		ptr = ptr -> prev;
	while (ptr)
	{
		printf("%d\n", ptr->num);
		num++;
		ptr = ptr->next;
	}
	return (num);
}
