#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if a singly-linked list contains a cycle
 * @list: A singly-linked list
 * Return: 0 if no cycle present, 1 if cycle present
 */

int check_cycle(listint_t *list)
{
	listint_t *dog, *cat;

	if (list == NULL || list->next == NULL)
		return (0);

	dog = list->next;
	cat = list->next->next;

	while (dog && cat && cat->next)
	{
		if (dog == cat)
			return (1);

		dog = dog->next;
		cat = cat->next->next;
	}

	return (0);
}
