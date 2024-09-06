package lab1;

public class Recursion {
 
	//Ex1.
	static int subsum(int n) {
		return subsum(n,0); 
    }
	static int subsum(int n, int acc){
		if (n==1) return acc+1; //base case
		if (n%2==0) return subsum(n-1,acc-n);
		return subsum(n-1,acc+n);
	}


    //Ex2.
	static int sumDigit(int n) { 
        return sumDigit(n,0);
    }
	static int sumDigit(int n, int sum){
		if (n<10) return sum+n;
		return sumDigit(Math.floorDiv(n, 10), sum+n%10);
	}

	//Ex3.
	public static int sumEven(int n) {
		// Ex3. Complete the content of this method
    	if (n==0) return 0;
    	else if (n%2==0) return n + sumEven(n - 2);
        else return sumEven(n - 1);
	}


    
	public static void main(String[] args) {
          

        // Test Uncomment these lines below to test your subsum code
                
        System.out.println("Calculating subsum(10):");
		System.out.println("Your answer is "+subsum(10));
        System.out.println("The correct answer is -5");
        System.out.println("-----------------------"); 
            

        // Uncomment these lines below to test your sumDigit code
            
    	System.out.println("sumDigit(123456789)");
		System.out.println("Your answer is "+ sumDigit(123456789));
        System.out.println("The correct answer is 45");
        System.out.println("-----------------------"); 

        // Uncomment these lines below to test your sumEven code
            
        System.out.println("Calculating sumEven(10):");
        System.out.println("Your answer is " + sumEven(10));
        System.out.println("The correct answer is 30");
        System.out.println("-----------------------"); 

	    }
    
	}