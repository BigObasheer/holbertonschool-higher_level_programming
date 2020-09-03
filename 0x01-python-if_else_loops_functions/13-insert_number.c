#include "lists.h"
/*
 * insert_node - inserts a new node sorted by
 * numeric weight
 * @head: address of head
 * @number: data to add to the new node
 * Return: NULL | newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *secondhalf;

	if (*head == NULL || head == NULL)
		return (NULL);

	if (new == NULL)
	{
		free(new);
		return (NULL);
	}

	for (; temp->next->n <= number; temp = temp->next)
	{
		;
	}

	secondhalf = temp->next;
	temp->next = new;
	new->n = number;
	new->next = secondhalf;

	return(new);
}
