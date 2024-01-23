
public class TestRectangle {
	public static void main(String[] args) {
		//1
		Rectangle box1 = new Rectangle();
		//2
		box1.printBasicInfo();
		//3
		System.out.println("Perimeter: "+box1.findPerimeter());
		//4
		System.out.println("Diagonal: "+box1.findDiagonal());
		//5
		if (box1.isSquare()) System.out.println("It is a square box");
		else System.out.println("It is not a square box");
		
		//6
		Rectangle box2 = new Rectangle(3,4);
		box2.printBasicInfo();
		System.out.println("Perimeter: "+box2.findPerimeter());
		System.out.println("Diagonal: "+box2.findDiagonal());
		if (box2.isSquare()) System.out.println("It is a square box");
		else System.out.println("It is not a square box");
	}
}
