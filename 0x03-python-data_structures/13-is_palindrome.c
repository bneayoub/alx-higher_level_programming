#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	listint_t *curr = *head;
	static listint_t *tmp;

	if (curr == NULL)
		return (1);

	if (tmp == NULL)
		tmp = curr;

	if (is_palindrome(&curr->next) && tmp->n == curr->n)
	{
		tmp = tmp->next;
		return (1);
	}
	else
		return (0);
}