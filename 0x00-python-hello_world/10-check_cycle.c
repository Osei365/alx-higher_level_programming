#include "lists.h"
#include <stdlib.h>
/**
 * check_cyle - checks if a linkedlist is a cycle
 * @list: linked list
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *comp1, *comp2;

	if (list == NULL)
	{
		return (0);
	}
	comp1 = list;
	comp2 = list->next;
	while (comp1 != NULL && comp2 != NULL && comp2->next)
	{
		if (comp1 == comp2)
			return (1);
		comp1 = comp1->next;
		comp2 = comp2->next->next;
	}
	return (0);
}
