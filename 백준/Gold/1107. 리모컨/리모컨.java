import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	int N, M;
	boolean[] has_num;
	
	public int canPush(int n) {
		if(n == 100) return 0;
		if(n < 0) return -1;
		String str = Integer.toString(n);
		for(int i=0;i<str.length();i++) {
			if(has_num[str.charAt(i) - '0'] == false)
				return -1;
		}
		return str.length();
	}
	
	public int pushCnt(int n) {
		int diff_ch = 0;
		int result=0;
		int base_result = canPush(n);
		if(n == 100)
			return 0;
		if(base_result != -1)
			return diff_ch + base_result;
		while(true) {
			diff_ch++;
			int near_ch;
			
			near_ch = canPush(n - diff_ch);
			if(near_ch != -1) {
				result = diff_ch + near_ch;
				break;
			}
			
			near_ch = canPush(n + diff_ch);
			if(near_ch != -1) {
				result = diff_ch + near_ch;
				break;
			} 
		}
		
		return result;
	}
	
	public void solution() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
			
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		st = new StringTokenizer(br.readLine());
		M = Integer.parseInt(st.nextToken());
		has_num = new boolean[10];
		Arrays.fill(has_num, true);
		if(M>0) {
			st = new StringTokenizer(br.readLine());
			for(int i=0;i<M;i++) {
				int t = Integer.parseInt(st.nextToken());
				has_num[t] = false;
			}
		}
		
		int res = pushCnt(N);
		int res_100 = Math.abs(N - 100);
		res = Math.min(res, res_100);
		
		sb.append(res);
		
		System.out.print(sb);
	}

	public static void main(String[] args) throws IOException{
		new Main().solution();	
	}
}
