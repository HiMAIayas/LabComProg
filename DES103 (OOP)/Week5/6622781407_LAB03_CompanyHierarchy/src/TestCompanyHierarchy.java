
public class TestCompanyHierarchy {
	public static void main(String[] args) {
		// a)
		System.out.println("### SOME COMPANY INFORMATION ###\n");
		
		// b)
		Person person01 = new Person("Somyai","Yodyium",15,4,1987);
		Person person02 = new Person("Pitak","Raksa",1,8,1980);
		System.out.println(">> Visitor Information");
		person01.printInfo();
		System.out.println("-------------------------");
		person02.printInfo();
		System.out.println("-------------------------\n");
		
		// c)
		Employee employee01 = new Employee("Maneeya","Rinrom",15,4,1987,"FutureTech CO.","Secretary",15000.0);
		Employee employee02 = new Employee("Parinya","Yenjid",5,11,1990,"FutureTech CO.","Technician",22000.0);
		System.out.println(">> Employee Information");
		employee01.printInfo();
		System.out.println("-------------------------");
		employee02.printInfo();
		System.out.println("-------------------------\n");
		
		// d)
		Executive executive01 = new Executive("Preecha","Yanusit",30,4,1977,"FutureTech CO.","Sale Manager",40000.0,80000.0);
		Executive executive02 = new Executive("Songpol","Sangar",10,11,1972,"FutureTech CO.","Finance Manager",38000.0,76000.0);
		System.out.println(">> Executive Information");
		executive01.printInfo();
		System.out.println("-------------------------");
		executive02.printInfo();
		System.out.println("-------------------------\n");
		
		// e)
		System.out.println(">> Rule Announcement");
		executive01.announceRule("No nap during working hours");
		
		// f)
		System.out.println("\n>>Rule Follower");
		employee01.followRule("No nap during working hours");
		employee02.followRule("No nap during working hours");
		
		// g)
		CEO ceo0 = new CEO("Sipol","Tongyai",19,9,1956,"FutureTech CO.","President",150000.0,500000.0,"BMW A5");
		System.out.println("\n>> CEO Information");
		ceo0.printInfo();
		
		// h)
		System.out.println("\n>> CEO Vision");
		ceo0.showVision("becoming ISO standard");
		
		// i)
		System.out.println("\n>> Number Of Person");
		Person.printNumberOfPerson();
		
	}
}
