// ���� ���ڸ� XOR �ϸ� ������ 0�� �ȴ�.
// ����, ¦����� 0�̵ȴ�.
// ��� XOR�ϸ� �ȴ�.

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

		free(nums);

		printf("Case #%d\n", test_case + 1);
		printf("%d\n", Answer);

	}

	return 0;