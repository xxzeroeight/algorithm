package easy.greedy._12927;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 문제: 배수 스위치
 * 유형: 그리디
 * 난이도: S
 *
 * 시간복잡도: O(nlogn)
 *
 * 아이디어:
 * 1. 전체를 순회하면서 해당 인덱스의 배수 번호의 상태를 모두 반전시킨다.
 *
 * 주의할 점/예외 케이스:
 * i번 스위치는 i의 배수 번호를 가지는 전구의 상태를 모두 반전시킨다. (끈다 X)
 * 전구는 모두 끌 수 있다.
 *
 * 시간 내/외: 내
 */

public class Main
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        char[] arr = s.toCharArray();

        int cnt = 0;
        for (int i=1; i<=arr.length; i++){

            if (arr[i-1] == 'Y') {
                for (int j=i-1; j<arr.length; j+=i) {
                    if (arr[j] == 'Y') arr[j] = 'N';
                    else arr[j] = 'Y';

                    // arr[j] = (arr[j] == 'Y') ? 'N' : 'Y';
                }

                cnt++;
            }
        }

        // YYYN YYYN YYYN YYNY YYYN
        // NNNY NNNY NNNY NNYN NNNY 1의 배수 반전 결과 (모두 다)
        // NNNN NNNN NNNN NNYY NNNN 4의 배수 반전 결과
        // NNNN NNNN NNNN NNNY NNNN 15의 배수 반전 결과
        // NNNN NNNN NNNN NNNN NNNN 16의 배수 반전 결과

        System.out.println(cnt);
    }
}
