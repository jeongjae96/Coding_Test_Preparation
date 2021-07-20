#include <stdio.h>
#include <stdlib.h>

// stdlib에 있는 qsort 함수에 사용될 compare 함수. 내림차순으로 정렬한다.
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

		// 과목의 수 N과 공부할 수 있는 과목의 수 K 입력.
		int N, K;
		scanf("%d %d", &N, &K);

		// 해당하는 과목을 공부했을 때, 받을 수 있는 점수 입력.
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