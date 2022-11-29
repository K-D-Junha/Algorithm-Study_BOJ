import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

class Square{
	int row, col;
	public Square(int row, int col) {
		this.row = row;
		this.col = col;
	}
}

class Snake{
	final static int UP = 0;
	final static int RIGHT = 1;
	final static int DOWN = 2;
	final static int LEFT = 3;
	int[][] board;
	int dir;
	ArrayDeque<Square> body;
	
	public Snake(int n) {
		body = new ArrayDeque<Square>();
		dir = RIGHT;
		board = new int[n+2][n+2];
		for(int[] a:board)
			Arrays.fill(a, 0);
		Square s = new Square(1,1);
		body.offerFirst(s);
	}
	
	public void turnDir(char c) {
		if(c == 'L') {
			if(this.dir == UP)
				this.dir = LEFT;
			else
				this.dir  = this.dir - 1;
		} else {
			if(this.dir == LEFT)
				this.dir = UP;
			else
				this.dir = this.dir + 1;
		}
	}
	
	public Square moveHead() {
		Square current_head = body.getFirst();
		Square next_head;
		if(this.dir == UP) {
			next_head = new Square(current_head.row-1, current_head.col);
		} else if(this.dir == RIGHT) {
			next_head = new Square(current_head.row, current_head.col+1);
		} else if(this.dir == DOWN) {
			next_head = new Square(current_head.row+1, current_head.col);
		} else {
			next_head = new Square(current_head.row, current_head.col-1);
		}
		body.offerFirst(next_head);
		board[next_head.row][next_head.col]++;
		return next_head;
	}
	
	public void moveTail() {
		Square s = body.pollLast();
		board[s.row][s.col]--;
	}
	
	public boolean checkEnd(int n) {
		Square s = body.getFirst();
		if(board[s.row][s.col] > 1)
			return true;
		if(s.row<1 || s.row>n || s.col<1 || s.col>n)
			return true;
		return false;
	}
}

class Turn{
	int second;
	char LR;
	
	public Turn(int second, char LR) {
		this.second = second;
		this.LR = LR;
	}
}

public class Main {
	int N, K, L;
	boolean[][] apples;
	ArrayList<Turn> turns;
	Snake snake;
	
	public void solution() throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		StringBuilder Sbuilder = new StringBuilder();
			
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		snake = new Snake(N);
		st = new StringTokenizer(br.readLine());
		K = Integer.parseInt(st.nextToken());
		apples = new boolean[N+2][N+2];
		for(boolean a[]: apples)
			Arrays.fill(a, false);
		for(int i=0;i<K;i++) {
			st = new StringTokenizer(br.readLine());
			int row = Integer.parseInt(st.nextToken());
			int col = Integer.parseInt(st.nextToken());
			apples[row][col] = true;
		}
		st = new StringTokenizer(br.readLine());
		L = Integer.parseInt(st.nextToken());
		turns = new ArrayList<Turn>();
		for(int i=0;i<L;i++) {
			st = new StringTokenizer(br.readLine());
			int sec = Integer.parseInt(st.nextToken());
			char c = st.nextToken().charAt(0);
			Turn t = new Turn(sec, c);
			turns.add(t);
		}
		
		int second_now = 0;
		while(true) {
			second_now++;
			Square head = snake.moveHead();
			
			boolean is_end = snake.checkEnd(N);
			if(is_end == true)
				break;
			
			if(apples[head.row][head.col] == true) {
				apples[head.row][head.col] = false;
			} else {
				snake.moveTail();
			}
			
			if(turns.size()>0) {
				Turn t = turns.get(0);
				if(second_now == t.second) {
					snake.turnDir(t.LR);
					turns.remove(0);
				}
			}							
		}
		
		sb.append(second_now);
		
		System.out.print(sb);
	}

	public static void main(String[] args) throws IOException{
		new Main().solution();	
	}
}
