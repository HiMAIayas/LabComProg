
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import java.lang.Math;
import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class BMICalculator extends JPanel{
    JPanel hwPanel = new JPanel(new GridLayout(2,2));
    JPanel resultPanel = new JPanel(new GridLayout(2,1));
    JPanel mainPanel = new JPanel(new GridLayout(3,1));
    JTextField weightInput = new JTextField(10); 
    JTextField heightInput = new JTextField(10); 
    JButton BMIBtn = new JButton("Compute BMI");
    JLabel resultText = new JLabel("BMI = ");

    



    BMICalculator(){
        
        addComponents();
        BMIBtn.addActionListener(new ActionInterpretor());



    }

    void addComponents(){
        setLayout(new BorderLayout());

        hwPanel.add(new JLabel("Your height (cm): "));
        hwPanel.add(heightInput);
        hwPanel.add(new JLabel("Your weight (cm): "));
        hwPanel.add(weightInput);

        resultPanel.add(BMIBtn);
        resultPanel.add(resultText);

        mainPanel.add(new JLabel("Enter your information"));
        mainPanel.add(hwPanel);
        mainPanel.add(resultPanel);

        add(mainPanel);
    }



    class ActionInterpretor implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            if (weightInput.getText().isEmpty() || heightInput.getText().isEmpty()){
                resultText.setText("Please Enter weight and height");
            }
            else{
                double weight = Double.parseDouble(weightInput.getText());
                double height = Double.parseDouble(heightInput.getText()); 
                resultText.setText("BMI = "+ weight/Math.pow(height/100,2));
            }

            
        }

    }
}
