#include "lists.h"
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - insert a node inside a sorted list
 * @head: head of the list
 * @number: the number to add within a list
 * Return: the new Node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	else if (number <= (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		current = *head;
		while (current->next && current->next->n < number)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
		return (new);
	}
}
