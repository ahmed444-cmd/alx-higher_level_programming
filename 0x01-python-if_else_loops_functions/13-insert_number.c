#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted sing-linkd lst.
 * @head: pointer to head of the linkd lst.
 * @number: numb to insert.
 * Return: If the function fails=>0 else pointer to the new nd.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
