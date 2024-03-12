import java.awt.*;
import javax.swing.*;

//Inherit appropriate superclass 
public class BarPanel extends JPanel{
	public BarPanel() {
        setLayout(new BorderLayout());
		add(new TextField("Ch 35 Vol 45"),BorderLayout.WEST);
		add(new ControlPanel());

	}
}
