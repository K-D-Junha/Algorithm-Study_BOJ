import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	StringBuilder sb;
	int N;
	ArrayList<ArrayList<Integer>> nums;
	ArrayList<ArrayList<Integer>> cache;
	
	public void solution() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		nums = new ArrayList<ArrayList<Integer>>();
		for(int i=0;i<N;i++) {
			ArrayList<Integer> al = new ArrayList<Integer>();
			nums.add(al);
		}
		for(int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0;j<(i+1);j++) {
				nums.get(i).add(Integer.parseInt(st.nextToken()));
			}
		}
		cache = new ArrayList<ArrayList<Integer>>();
		for(int i=0;i<N;i++) {
			ArrayList<Integer> al = new ArrayList<Integer>();
			cache.add(al);
		}
		
		cache.get(0).add(nums.get(0).get(0));
		for(int i=1;i<N;i++) {
			ArrayList<Integer> alist = cache.get(i);
			ArrayList<Integer> uplist = cache.get(i-1);
			alist.add(uplist.get(0) + nums.get(i).get(0));
			for(int j=1;j<i;j++) {
				int up_left = uplist.get(j-1);
				int up_right = uplist.get(j);
				if(up_left>up_right) {
					alist.add(up_left + nums.get(i).get(j));
				} else {
					alist.add(up_right + nums.get(i).get(j));
				}
			}
			alist.add(uplist.get(i-1) + nums.get(i).get(i));
		}
		
		int max = -1;
		ArrayList<Integer> alist = cache.get(N-1);
		for(int i=0;i<N;i++) {
			int num = alist.get(i);
			if(max < num)
				max = num;
		}
		sb.append(max);
		System.out.print(sb);
	}

	public static void main(String[] args) throws IOException{
		new Main().solution();	
	}
}