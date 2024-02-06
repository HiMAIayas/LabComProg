
public class Name {
	String firstname;
	String lastname;
	
	Name(String firstname, String lastname){
		this.firstname = firstname;
		this.lastname = lastname;
	}
	
	void printName() {
		System.out.println("Name: "+firstname+" "+lastname);
	}
}
