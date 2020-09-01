#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list - singly linked list
 */

int check_cycle(listint_t *list)
{
	listint_t *hare = list, *tor = list;

	while(tor)
	{
		tor = tor->next;
		hare = hare->next->next;
		if (tor == hare)
			return(1);
	}
	return (0);
}
