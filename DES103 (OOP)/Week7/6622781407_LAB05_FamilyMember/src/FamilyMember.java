public class FamilyMember {
    static String familyName = "Hilton";
	String firstname;
	static double commonFund = 100000.00;
	double privateFund;
	
	FamilyMember(String firstname, double privateFund){
		this.firstname = firstname;
		this.privateFund = privateFund;
	}
	
	void printPrivateFund() {
		System.out.println(firstname+" has $"+privateFund);
	}

    void contributeToCommonFund(double amount){
        if (amount>privateFund) System.out.println("Not enough money to contribute");
        else {
            privateFund-=amount;
            FamilyMember.commonFund+=amount;
        }
    }

    static void payFromCommonFund(double amount){
        if (amount>commonFund) System.out.println("You don't have enough money in your common fund");
        else {
            commonFund-=amount;
        }
    }
}
