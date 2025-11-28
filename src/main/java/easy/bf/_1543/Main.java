package easy.bf._1543;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

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
