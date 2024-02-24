#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev_slow = NULL, *mid = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return 1; // Empty list or single node is considered a palindrome

    // Move fast and slow pointers to find the middle of the linked list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        prev_slow = slow;
        slow = slow->next;
    }

    // If the linked list has an odd number of nodes, skip the middle one
    if (fast != NULL)
    {
        mid = slow;
        slow = slow->next;
    }

    // Reverse the second half of the linked list
    prev_slow->next = NULL;
    reverse_list(&slow);

    // Compare the first half with the reversed second half
    is_palindrome = compare_lists(*head, slow);

    // Restore the linked list to its original state
    reverse_list(&slow);
    if (mid != NULL)
    {
        prev_slow->next = mid;
        mid->next = slow;
    }
    else
    {
        prev_slow->next = slow;
    }

    return is_palindrome;
}

/**
 * reverse_list - reverses a linked list
 * @head: pointer to the head of the linked list
 */
void reverse_list(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    *head = prev;
}

/**
 * compare_lists - compares two linked lists
 * @list1: pointer to the head of the first linked list
 * @list2: pointer to the head of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *list1, listint_t *list2)
{
    while (list1 != NULL && list2 != NULL)
    {
        if (list1->n != list2->n)
            return 0;

        list1 = list1->next;
        list2 = list2->next;
    }

    return (list1 == NULL && list2 == NULL);
}
