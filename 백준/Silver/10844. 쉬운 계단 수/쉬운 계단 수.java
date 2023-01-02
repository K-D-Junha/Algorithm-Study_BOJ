import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	StringBuilder sb;
	int N;
	int[][] cache;
	final int MOD_NUM = 1000000000;
	
	public int modPlus(int a, int b) {
		return ((a % MOD_NUM) + (b % MOD_NUM)) % MOD_NUM;
	}
	
	public void solution() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		cache = new int[N+1][10];
		cache[1][0] = 0;
		for(int i=1;i<10;i++)
			cache[1][i] = 1;
		
		for(int n=2;n<=N;n++) {
			cache[n][0] = cache[n-1][1];
			for(int i=1;i<=8;i++) {
				cache[n][i] = this.modPlus(cache[n-1][i-1], cache[n-1][i+1]);
			}
			cache[n][9] = cache[n-1][8];
		}
		
		int ans = cache[N][0];
		for(int i=1;i<10;i++) {
			ans = this.modPlus(ans,cache[N][i]);
		}
		
		sb.append(ans);
		System.out.print(sb);
	}

	public static void main(String[] args) throws IOException{
		new Main().solution();	
	}
}