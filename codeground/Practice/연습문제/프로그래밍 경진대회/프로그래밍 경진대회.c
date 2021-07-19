#include <stdio.h>
#include <stdlib.h>

//stdlib �� �ִ� qsort�Լ��� ���� compare �Լ�. ������������ sorting�Ѵ�.
int cmp(const void* a1, const void* a2)
{
	return *(int*)a1 - *(int*)a2;
}


//�ִ� ã��
int MAX(int* arr, int n)
{
	int max = 0;

	for (int i = 0; i < n; i++)
	{
		if (arr[i] > max) max = arr[i];
	}

	return max;
}

// int Answer;

int main(void)
{
	int T, test_case;

	setbuf(stdout, NULL);

	scanf("%d", &T);
	for (test_case = 0; test_case < T; test_case++)
	{

		// �������� �� N �Է�.
		int N;
		scanf("%d", &N);

		// �������� ������ ���� ������ ���� ������ �� �Է�.
		int* score = (int*)malloc(sizeof(int) * N);

		for (int i = 0; i < N; i++)
		{
			scanf("%d", &score[i]);
		}

		// �������� ���� �������� ����.
		qsort(score, N, sizeof(int), cmp);

		// ������ ���� �������� ������ ������ ���� ���� �ջ�.
		int* total_score = (int*)malloc(sizeof(int) * N);

		for (int i = 0; i < N; i++)
		{
			total_score[i] = score[i] + N - i;
		}

		// ���� �� ���� ū �� ã��.
		int max = MAX(total_score, N);

		// ����� �� �ִ� �������� �� ���ϱ�.
		int count = 0;

		for (int i = 0; i < N; i++)
		{
			if (score[i] + N >= max)
				count += 1;
		}

		// ���� �Ҵ� �޸� ����.
		free(score);
		free(total_score);

		printf("Case #%d\n", test_case + 1);
		printf("%d\n", count);

	}

	return 0;
}