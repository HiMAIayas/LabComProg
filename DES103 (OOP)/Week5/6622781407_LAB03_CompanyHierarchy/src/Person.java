
public class Person {
	Name name;
	Date dateOfBirth;
	static int numPerson=0;
	
	Person(String firstname, String lastname, int day, int month, int year){
		this.name = new Name(firstname,lastname);
		this.dateOfBirth = new Date(day, month, year);
		Person.numPerson++;
	}
	
	void printInfo() {
		name.printName();
		dateOfBirth.printDate();
		printAgeAtYear(2024);
	}
	
	void printAgeAtYear(int year) {
		System.out.println("Age: "+(year-dateOfBirth.year));
	}
	
	static void printNumberOfPerson() {
		System.out.println("The total number of Persons is "+numPerson);
	}
}
