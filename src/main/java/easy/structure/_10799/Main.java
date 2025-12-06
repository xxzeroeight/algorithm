package easy.structure._10799;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

/**
 * 문제: 쇠막대기
 * 유형: 자료구조/스택
 * 난이도: S
 *
 * 시간복잡도: O(n)
 *
 * 아이디어:
 * 1. 레이저를 만났을 때
 *  1-1. 현재까지 모아놨던 막대기의 개수-1을 카운트한다.
 * 2. 막대기의 끝
 *  2-1. 마지막 ")"을 카운트한다.
 *
 * 주의할 점/예외 케이스:
 *
 *
 * 시간 내/외: 외
 */

public class Main
{
    public static void main(String[] args) throws IOException {
        /* 입력 처리 */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        Stack<Character> stack = new Stack<>();

        /* 핵심 로직 */
        int ans = 0;
        int tmp = 0;

        for (int i=0; i<str.length(); i++){
            if (stack.isEmpty() || str.charAt(i) == '('){
                stack.push('(');
                tmp++;
            } else if (str.charAt(i) == ')') {
                if (str.charAt(i-1) == '(') {
                    stack.pop();
                    tmp--;
                    ans += tmp;
                } else if (str.charAt(i-1) == ')') {
                    ans++;
                    tmp--;
                    stack.pop();
                }
            }
        }

        /* 결과 출력 */
        System.out.println(ans);
    }
}
