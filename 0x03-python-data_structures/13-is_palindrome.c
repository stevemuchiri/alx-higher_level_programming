#include "lists.h"

/**
 * reverse_list - Reverses a linked list
 * @head: Pointer to the head of the linked list
 * Return: Pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
		listint_t *prev = NULL;
		listint_t *current = head;
		listint_t *next = NULL;

		while (current != NULL)
		{
			next = current->next;
			current->next = prev;
			prev = current;
			current = next;
		}

		return (prev);
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *second_half;
	listint_t *mid;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
		slow = slow->next;

		second_half = reverse_list(slow);
		mid = second_half;

	while (*head != NULL && second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			reverse_list(mid);
			return (0);
			}
		*head = (*head)->next;
		second_half = second_half->next;
	}
	reverse_list(mid);

	return (1);
}
