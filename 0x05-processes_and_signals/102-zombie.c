#include <stdio.h>
#include <unistd.h>


/**
 *infinite_while - infinite while loop
 *@void: no input parameter
 *Return: 0 on succes
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 *main - creates 5 zombie process
 *@void: no input parameter
 *Return: void
 */
int main(void)
{
	int i, zombie_pid;

	for (i = 0; i < 5; i++)
	{
		zombie_pid = fork();
		if (zombie_pid > 0)
			printf("Zombie process created, PID: %d\n", zombie_pid);
		else
			return (0);
	}
	infinite_while();
	return (0);
}
