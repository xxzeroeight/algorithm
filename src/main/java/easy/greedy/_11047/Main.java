package easy.greedy._11047;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 문제: 동전 0
 * 유형: 그리디
 * 난이도: S
 *
 * 시간복잡도: O(nlogn)
 *
 * 아이디어:
 * 1. 동전을 거슬러 줄 때, 동전 개수의 최소로 하기위해서는 단위가 큰 것부터 거슬러준다.
 *
 * 주의할 점/예외 케이스:
 *
 *
 * 시간 내/외: 내
 */

public class Main
{
    public static void main(String[] args) throws IOException {
        /* 입력 처리 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());

        /* 핵심 로직 */
        int[] coins = new int[n];
        for (int i=0; i<n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(coins);

        int cnt = 0;
        for (int i=n-1; i>=0; i--) {
            cnt += target / coins[i]; // 4200 / 1000의: 4
            target %= coins[i]; // 4200 % 1000: 200
        }

        /* 결과 출력 */
        System.out.println(cnt);
    }
}
