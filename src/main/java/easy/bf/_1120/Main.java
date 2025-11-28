package easy.bf._1120;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 문제: 문자열
 * 유형: 브루트포스/문자열
 * 난이도: S
 *
 * 시간복잡도: O(N × M)
 *
 * 아이디어:
 * 1. 추가된 문자열은 모든 비교에서 무조건 차이에 포함되므로 무시한다.
 * 2. a를 b의 시작부터 끝까지 한 칸씩 이동하면서 겹치는 부분을 비교한다.
 * 3. 1, 2번의 내용으로 미루어보아 슬라이딩 윈도우 방식이다.
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

        String[] input = br.readLine().split(" ");
        String a = input[0];
        String b = input[1];

        // "*adaabc", "adaabc*"
        // "*koder**", "koder***"

        /* 핵심 로직 */
        int minCnt = Integer.MAX_VALUE;

        for (int i=0; i<b.length() - a.length() + 1; i++) {
            String s = b.substring(i, i+a.length()); // b문자열에서 a길이만큼 추출(aababb, ababbc)

            int cnt = 0;
            for (int j=0; j<a.length(); j++) { // ("aababb", "adaabc"), ("ababbc", "adaabc")
                if (s.charAt(j) != a.charAt(j)) { cnt++; }
            }

            minCnt = Math.min(minCnt, cnt);
        }

        /* 결과 출력 */
        System.out.println(minCnt);
    }
}
