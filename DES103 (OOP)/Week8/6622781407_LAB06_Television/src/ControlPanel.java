import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JPanel;

//Inherit appropriate superclass 
public class ControlPanel extends JPanel{
    AdjustPanel pCh = new AdjustPanel("Ch");
    AdjustPanel pVol = new AdjustPanel("Vol");

	public ControlPanel() {		
		setLayout(new GridLayout(1,3));

		add(pCh);
        add(pVol);


        JButton on_off_btn = new JButton("On/Off");
        add(new JButton("On/Off"));

	}
}