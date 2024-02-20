public class FamilyMemberTesting {
	public static void main(String[] args) {
		
		//Exercise 2-a: use  the dot operator to print out  familyName with commonFund
        System.out.println("# COMMON FUND OF THE FAMILY");
		System.out.println("The "+FamilyMember.familyName+" family has $"+FamilyMember.commonFund);
		
        //Exercise 2-b: create an array arrayFamily for adding four members.
        
		FamilyMember[] arrayFamily = {
            new FamilyMember("John", 254639.12),
            new FamilyMember("Erika", 187346.56),
            new FamilyMember("James", 56783.12),
            new FamilyMember("Paris", 12124.88)

        };
        System.out.println("-------------------------- \n");

		//Exercise 2-b: print private fund for all family members.
        System.out.println("# PRIVATE FUND");
        for (FamilyMember member:arrayFamily){
            member.printPrivateFund();
        }



		

		System.out.println("-------------------------- \n");

		//Exercise 3-b: contribute private fund to common fund
		System.out.println("# CONTRIBUTION OF PRIVATE FUND");
		arrayFamily[1].contributeToCommonFund(10000);
        arrayFamily[3].contributeToCommonFund(10000);
        for (FamilyMember member:arrayFamily){
            member.printPrivateFund();
        }
		System.out.println("-------------------------- \n");
		
		//Exercise 3-d: print the updated common fund of the family.
		System.out.println("# UPDATED COMMON FUND OF THE FAMILY");
        System.out.println("The "+FamilyMember.familyName+" family has $"+FamilyMember.commonFund);
		System.out.println("-------------------------- \n");

	}

}