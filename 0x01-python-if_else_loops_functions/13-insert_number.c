#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert node
 * @head: had of linked list
 * @number: number to insert
 * Return: address of inked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new, *ptr;

	ptr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (new->n < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (ptr != NULL)
	{
		temp = ptr;
		ptr = ptr->next;
		if (new->n < ptr->n)
		{
			temp->next = new;
			new->next = ptr;
			return (*head);
		}
	}
	return (NULL);
}
