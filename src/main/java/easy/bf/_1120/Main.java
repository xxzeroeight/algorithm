package easy.bf._1120;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        String a = input[0];
        String b = input[1];

        int minCnt = Integer.MAX_VALUE;

        for (int i=0; i<b.length() - a.length() + 1; i++) {
            String s = b.substring(i, i+a.length());

            int cnt = 0;
            for (int j=0; j<a.length(); j++) {
                if (s.charAt(j) != a.charAt(j)) { cnt++; }
            }

            minCnt = Math.min(minCnt, cnt);
        }

        System.out.println(minCnt);
    }
}
