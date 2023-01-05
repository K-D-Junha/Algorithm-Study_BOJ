import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	StringBuilder sb;
	int N;
	int[] cache_oo;
	int[] cache_xo;
	int[] wines;
	
	public void solution() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		cache_oo = new int[N+1];
		cache_xo = new int[N+1];
		wines = new int[N+1];
		for(int i=1;i<=N;i++) {
			wines[i] = Integer.parseInt(br.readLine());
		}
		
		int ans;
		if(N==1) {
			ans = wines[1];
		} else if(N==2) {
			ans = wines[1]+wines[2];
		} else {
			cache_oo[1] = cache_xo[1] = wines[1];
			cache_oo[2] = wines[1] + wines[2]; cache_xo[2] = wines[2];
			cache_oo[3] = wines[2] + wines[3];
			cache_xo[3] = wines[1] + wines[3];
			
			for(int i=4;i<=N;i++) {
				cache_oo[i] = cache_xo[i-1] + wines[i];
				cache_xo[i] = Math.max((Math.max(cache_oo[i-2], cache_xo[i-2]) + wines[i]), (cache_oo[i-3]+wines[i]));
			}
			
			ans = cache_oo[N-1];
			if(cache_xo[N-1]>ans) ans = cache_xo[N-1];
			if(cache_oo[N]>ans) ans = cache_oo[N];
			if(cache_xo[N]>ans) ans = cache_xo[N];
		}
		
		sb.append(ans);
		System.out.print(sb);
	}

	public static void main(String[] args) throws IOException{
		new Main().solution();	
	}
}