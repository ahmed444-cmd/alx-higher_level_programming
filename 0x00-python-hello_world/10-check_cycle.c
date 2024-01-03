#include "lists.h"

/**
 * check_cycle - check a linkd lst containing a cycle
 * @list: the linkd lst
 *
 * Return: 1 if the lst has a cycle, else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
