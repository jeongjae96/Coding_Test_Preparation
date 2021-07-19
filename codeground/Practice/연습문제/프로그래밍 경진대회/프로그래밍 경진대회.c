#include <stdio.h>
#include <stdlib.h>

//stdlib 에 있는 qsort함수에 사용될 compare 함수. 오름차순으로 sorting한다.
int cmp(const void* a1, const void* a2)
{
	return *(int*)a1 - *(int*)a2;
}


//최댓값 찾기
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

		// 응시자의 수 N 입력.
		int N;
		scanf("%d", &N);

		// 응시자의 마지막 라운드 전까지 받은 점수의 합 입력.
		int* score = (int*)malloc(sizeof(int) * N);

		for (int i = 0; i < N; i++)
		{
			scanf("%d", &score[i]);
		}

		// 응시자의 점수 오름차순 정렬.
		qsort(score, N, sizeof(int), cmp);

		// 마지막 라운드 전까지의 점수와 마지막 라운드 점수 합산.
		int* total_score = (int*)malloc(sizeof(int) * N);

		for (int i = 0; i < N; i++)
		{
			total_score[i] = score[i] + N - i;
		}

		// 점수 중 제일 큰 값 찾기.
		int max = MAX(total_score, N);

		// 우승할 수 있는 응시자의 수 구하기.
		int count = 0;

		for (int i = 0; i < N; i++)
		{
			if (score[i] + N >= max)
				count += 1;
		}

		// 동적 할당 메모리 해제.
		free(score);
		free(total_score);

		printf("Case #%d\n", test_case + 1);
		printf("%d\n", count);

	}

	return 0;
}