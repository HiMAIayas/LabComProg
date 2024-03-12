import java.awt.*;
import javax.swing.*;

//Inherit appropriate superclass 
public class AdjustPanel extends JPanel{

	public AdjustPanel(String centerText) {
		add(new JButton("<<"));
        add(new JButton(centerText));
        add(new JButton(">>"));
	}
}