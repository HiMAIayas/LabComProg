import java.awt.*;
import javax.swing.*;

public class Microwave extends JFrame {
	public Microwave() {
		super();
        setLayout(new BorderLayout());
        MicrowaveComponents();

		setSize(550,250);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		

	}
	
	public void MicrowaveComponents() {
		JPanel panel1 = new JPanel(new BorderLayout());
		
		JButton btn1 = new JButton("Food to be placed here");
		btn1.setBackground(Color.WHITE);

		JPanel panel11 = new JPanel(new GridLayout(4,3));

		panel1.add(new JTextField("Microwave Tmie Display"),BorderLayout.NORTH);

		for (int i=0; i<9; i++){
            panel11.add(new JButton(Integer.toString(i+1)));
        }
        panel11.add(new JButton("Stop"));
        panel11.add(new JButton("0"));
        panel11.add(new JButton("Start"));

		panel1.add(panel11);

		add(btn1);
		add(panel1,BorderLayout.EAST);
	}
}