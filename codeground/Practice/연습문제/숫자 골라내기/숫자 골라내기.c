// 같은 숫자를 XOR 하면 어차피 0이 된다.
// 따라서, 짝수라면 0이된다.
// 모두 XOR하면 된다.

#include <stdio.h>

int Answer;

int main(void)
{
	int T, test_case;

	setbuf(stdout, NULL);

	scanf("%d", &T);
	for (test_case = 0; test_case < T; test_case++)
	{
		int N;
		scanf("%d", &N);

		int* nums = (int*)malloc(sizeof(int) * N);

		for (int i = 0; i < N; i++)
			scanf("%d", &nums[i]);

		Answer = 0;

		for (int i = 0; i < N; i++)
		{
			Answer ^= nums[i];
		}


		printf("Case #%d\n", test_case + 1);
		printf("%d\n", Answer);

	}

	return 0;