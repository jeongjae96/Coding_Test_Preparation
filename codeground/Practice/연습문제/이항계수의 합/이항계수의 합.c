// 참고: https://blog.naver.com/skyshin0304/221332954543

#include <stdio.h>

#define P (int)1000000007

// 나올 수 있는 최대 팩토리얼이 (N+M+2)!이므로, 2,000,003까지 modulo P로 계산한 결과값을 배열에 저장.
long long int facto_modulo_arr[2000003];

void facto_modular(int max)
{

	facto_modulo_arr[0] = 1;


	for (int i = 1; i <= max; i++)
	{

		facto_modulo_arr[i] = (i * facto_modulo_arr[i - 1]) % P;

	}

}

long long int compute_B_1_mod(long long int x)
{

	long long int rem = 1;

	int power = P - 2;



	while (power > 0)
	{

		if (power % 2)
			rem = ((rem * x) % P);

		x = (x * x) % P;

		power /= 2;
	}

	return rem;
}

int main(void)
{
	facto_modular(2000002);

	int T, test_case;

	setbuf(stdout, NULL);

	scanf("%d", &T);
	for (test_case = 0; test_case < T; test_case++)
	{
		int N, M;

		scanf("%d %d", &N, &M);

		long long int A_mod_p, B_mod_p, Answer;

		A_mod_p = facto_modulo_arr[N + M + 2];

		B_mod_p = compute_B_1_mod((facto_modulo_arr[N + 1] * facto_modulo_arr[M + 1]) % P);

		Answer = (A_mod_p * B_mod_p) % P - 1;

		printf("Case #%d\n", test_case + 1);
		printf("%lld\n", Answer);

	}

	return 0;
}