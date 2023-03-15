#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "list.h"

/**
 * main - check the code
 *
 * Return: always 0.
 */
in main(void)
{
	listint_t *head;
	listint_t *current;
	lisint_t *temp;
	int i;

	head = NULL;
	add_nodeint(&head, 0);
	add_nodeint(&head, 1);
	add_nodeint(&head, 2);
	add_nodeint(&head, 3);
	add_nodeint(&head, 4);
	add_nodeint(&head, 98);
	add_nodeint(&head, 402);
	add_nodeint(&head, 1024);
	print_listint(head);

	if (check_cycle(head) == 0)
		printf("linked list has no cycle\n");
	else if (check_cycle(head) == 1)
		printf("linked list a cyclen\n");

	current = head;
	for (i = 0; i < 4; i++)
		current = current->next;
	current->next = temp;

	free_listint(head);

	return (0);
}
