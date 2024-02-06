
public class CEO extends Executive{
	String positionVehicle;
	
	CEO(String firstname, String lastname, int day, int month, int year, String workplace, String position, double salary,double bonus,String positionVehicle){
		super(firstname,lastname,day,month,year,workplace,position,salary,bonus);
		this.positionVehicle = positionVehicle;
	}
	
	void printInfo() {
		super.printInfo();
		System.out.println("PositionVehicle: "+this.positionVehicle);
	}
	
	void showVision(String vision) {
		System.out.println(
				super.name.firstname+" "+
				super.name.lastname + " shows " +
				vision);
	}
}
