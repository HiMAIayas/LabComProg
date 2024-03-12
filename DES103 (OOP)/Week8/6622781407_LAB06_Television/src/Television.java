import java.awt.*;
import javax.swing.*;

//Inherit appropriate superclass 
public class Television extends JFrame {
	JButton screen = new JButton();
	public Television(String title) {
		//Call a method TelevisionComponents
        super();
        setSize(640,400);
        setLayout(new BorderLayout());
        TelevisionComponents();
        setVisible(true);
		//set JFrame

	}
	
	public void TelevisionComponents() {
		//create abutton_TelevisionScreen and panal_TelevisionButtonBar
		screen.setBackground(Color.BLACK);
        add(screen);
		add(new BarPanel(),BorderLayout.SOUTH);

	}
}