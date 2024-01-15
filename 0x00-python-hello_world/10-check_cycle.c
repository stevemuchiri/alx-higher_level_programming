#include "lists.h"
#include <stdio.h>
/**
  * check_cycle - Checks if a singly linked list has a cycle 
  * @list: The singly linked list to check
  *
  * Return: 1 if has a cycle in it or 0 if not
  */
int check_cycle(listint_t *list)
{
	listint_t *string = list, *n = list;
	int found = 0;

	while ((string && n) && n->next)
	{		
		string = string->next;

		if (n->next || n->next->next)	
			n = n->next->next;
		else
			break;

		if (string == n)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
