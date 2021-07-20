#include <stdio.h>
#include <stdlib.h>

// stdlib�� �ִ� qsort �Լ��� ���� compare �Լ�. ������������ �����Ѵ�.
int cmp(const void* a1, const void* a2)
{
	return *(int*)a2 - *(int*)a1;
}

int main(void)
{
	int T, test_case;

	setbuf(stdout, NULL);

	scanf("%d", &T);
	for (test_case = 0; test_case < T; test_case++)
	{

		// ������ �� N�� ������ �� �ִ� ������ �� K �Է�.
		int N, K;
		scanf("%d %d", &N, &K);

		// �ش��ϴ� ������ �������� ��, ���� �� �ִ� ���� �Է�.
		int* score = (int*)malloc(sizeof(int) * N);

		for (int i = 0; i < N; i++)
		{
			scanf("%d", score + i);
		}

		qsort(score, N, sizeof(int), cmp);

		int sum = 0;

		for (int i = 0; i < K; i++)
		{
			sum += score[i];
		}

		free(score);

		printf("Case #%d\n", test_case + 1);
		printf("%d\n", sum);

	}

	return 0;
}