
public class Rectangle {
	double width;
	double length;
	
	Rectangle(){
		this.width = 1;
		this.length = 1;
	}
	
	Rectangle(double width, double length){
		this.width = width;
		this.length = length;
	}
	
	double findArea() {
		return width*length;
	}
	
	double findPerimeter() {
		return 2*width*length;
	}
	
	double findDiagonal() {
		return Math.sqrt(width*width + length*length);
	}
	boolean isSquare() {
		return width==length;
	}
	void printBasicInfo() {
		System.out.println("The width is "+width);
		System.out.println("The length is "+length);
	}
}
