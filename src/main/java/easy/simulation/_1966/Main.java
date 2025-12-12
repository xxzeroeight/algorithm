package easy.simulation._1966;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * 문제: 프린터 큐
 * 유형: 시뮬레이션/큐
 * 난이도: S
 *
 * 시간복잡도: O(t x n^2)
 *
 * 아이디어:
 * 1. 위치를 추적한다.
 *  1-1. 중요도와 위치를 함께 저장하면 추적하기 쉽다.
 *
 * 주의할 점/예외 케이스:
 *
 *
 * 시간 내/외: 내
 */

public class Main
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int t = Integer.parseInt(br.readLine());

        for (int i=0; i<t; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            Queue<int[]> q = new LinkedList<>();

            st = new StringTokenizer(br.readLine());
            for (int j=0; j<n; j++) {
                int num = Integer.parseInt(st.nextToken());

                q.add(new int[] { num, j }); // [[1, 0], [1, 1], [9, 2], [1, 3], [1, 4], [1, 5]]
            }

            int cnt = 0;
            while (!q.isEmpty()) {
                int[] current = q.peek();

                int mv = q.stream()
                        .mapToInt(p -> p[0])
                        .max()
                        .orElse(0);

                if (mv == current[0]) {
                    cnt++;

                    int[] tmp = q.poll();
                    if (tmp[1] == m) { // j == m
                        System.out.println(cnt);
                        break;
                    }
                } else q.add(q.poll());
            }
        }
    }
}
