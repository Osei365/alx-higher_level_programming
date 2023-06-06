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
	listint_t *new, *ptr;

	ptr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL || new->n < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (ptr != NULL && ptr->next != NULL && ptr->next->n < new->n)
	{
		ptr = ptr->next;
	}
	new->next = ptr->next;
	ptr->next = new;
	return (new);
}
