import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	StringBuilder sb;
	int N;
	int[] numbers;
	int[] operators;
	int[] oper_cnts;
	int min = 1198765432, max = -1198765432;
	
	public int calculate() {
		int res = numbers[0];
		
		for(int i=1;i<N;i++) {
			int op = operators[i-1], n2 = numbers[i];
			switch(op) {
			case 0:
				res += n2;
				break;
			case 1:
				res -= n2;
				break;
			case 2:
				res *= n2;
				break;
			case 3:
				res /= n2;
				break;
			}
		}
		
		return res;
	}
	
	public void dfs(int depth) {
		if(depth == N-1) {
			int res = this.calculate();
			if(max<res) max = res;
			if(min>res) min = res;
			return;
		}
		for(int i=0;i<4;i++) {
			if(oper_cnts[i]>0) {
				oper_cnts[i] -= 1;
				operators[depth] = i;
				this.dfs(depth+1);
				oper_cnts[i] += 1;
				operators[depth] = -1;
			}
		}
	}
	
	public void solution() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		oper_cnts = new int[4];
		numbers = new int[N];
		operators = new int[N-1];
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<N;i++) {
			numbers[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(br.readLine());
		for(int i=0;i<4;i++) {
			oper_cnts[i] = Integer.parseInt(st.nextToken());
		}
		
		this.dfs(0);
		
		sb.append(max+"\n"+min);
		System.out.print(sb);
	}

	public static void main(String[] args) throws IOException{
		new Main().solution();	
	}
}
