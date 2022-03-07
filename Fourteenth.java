package projecteuler;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Fourteenth {
	
	public static void main(String[] args) {
		int array[]=new int[2];
		array[0]=0;//chain
		array[1]=0;//number
		
		
		long x=0;
		int chain=1;
		for(int i=1;i<1000000;i++) {
			chain=1;
			x=i;
			while(x!=1) {
				if(x%2==1) {
					chain++;
					x=3*x+1;
				}else if(x%2==0) {
					chain++;
					x=x/2;
				}
			}
			if(chain>array[0]) {
				array[0]=chain;
				array[1]=i;
			}			
		}
		

		System.out.println(array[0]);
		System.out.println(array[1]);
		
	}

}
