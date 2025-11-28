package easy.bf._1543;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 문제: 문서 검색
 * 유형: 브루트포스/문자열
 * 난이도: S
 *
 * 시간복잡도: O(N × M)
 *
 * 아이디어:
 * 1. 현재 위치에서 단어를 찾은 경우
 *  1-1. 찾은 단어의 길이만큼 건너뛰기 (중복 X)
 * 2. 현재 위치에서 단어를 찾지 못한 경우
 *  2-1. 한 칸 이동
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

        String text = br.readLine();
        String find = br.readLine();

        int cnt = 0;
        int idx = 0;

        while (idx <= text.length() - find.length()) {
            if (text.substring(idx, idx + find.length()).equals(find)) {
                cnt++;
                idx += find.length();
            } else  idx++;
        }

        System.out.println(cnt);
    }
}
