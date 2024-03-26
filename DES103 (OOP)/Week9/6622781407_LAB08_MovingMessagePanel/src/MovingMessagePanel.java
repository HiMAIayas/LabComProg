import javax.swing.*;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.GridLayout;
import java.awt.event.*;


public class MovingMessagePanel extends JPanel implements ActionListener, ItemListener, MouseMotionListener{
    JFrame frame = new JFrame();
    Color textColor;

    JTextField textInput = new JTextField(30);
    JRadioButton whiteBtn = new JRadioButton("White");
    JRadioButton blackBtn = new JRadioButton("Black");

    ButtonGroup btnGroup = new ButtonGroup();

    JButton btnLeft = new JButton("Left");
    JButton btnRight = new JButton("Right");
    JButton btnUp = new JButton("Up");
    JButton btnDown = new JButton("Down");

    JRadioButton mouseBtn = new JRadioButton("Use Mouse");
    int[] pos = {0,250};




    MovingMessagePanel(){
        frame.setLayout(new BorderLayout());
        addComponents();
        textInput.addActionListener(this);
        whiteBtn.addItemListener(this);
        blackBtn.addItemListener(this);
        
        btnLeft.addActionListener(this);
        btnRight.addActionListener(this);
        btnUp.addActionListener(this);
        btnDown.addActionListener(this);

        this.addMouseMotionListener(this);

        
        frame.setVisible(true);
        frame.setSize(800,500);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    void moveMessage(ActionEvent e){
        if (e.getSource()==btnLeft) pos[0]-=5;
        else if (e.getSource()==btnRight) pos[0]+=5;
        else if (e.getSource()==btnUp) pos[1]-=5;
        else if (e.getSource()==btnDown) pos[1]+=5;
        repaint();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==textInput) repaint();
        else moveMessage(e);
    }



    @Override
    public void itemStateChanged(ItemEvent e) {
        if(e.getSource()==whiteBtn){
            textColor = Color.BLACK;
            this.setBackground(Color.WHITE);
            //blackBtn.setSelected(false);
        }
        else if(e.getSource()==blackBtn){
            textColor = Color.PINK;
            this.setBackground(Color.BLACK); 
            //whiteBtn.setSelected(false);
        }

        repaint();
    }
    @Override
    public void mouseDragged(MouseEvent e) {
        if (mouseBtn.isSelected()){
            pos[0]=e.getX();
            pos[1]=e.getY();
            repaint();
        }
        
    }

    @Override
    public void mouseMoved(MouseEvent e) {}

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setFont(new Font("SansSerif",Font.BOLD,100));
        g.setColor(textColor);
        g.drawString(textInput.getText(),pos[0],pos[1]);
    }






    void addComponents(){
        //Message Panel
        JPanel mesPanel = new JPanel();
        mesPanel.add(new JLabel("Message:"));
        mesPanel.add(textInput);
        frame.add(mesPanel, BorderLayout.NORTH);

        //Color Panel
        JPanel colPanel = new JPanel(new GridLayout(3,1));
        colPanel.add(new JLabel("Background Color"));
        btnGroup.add(whiteBtn);
        colPanel.add(whiteBtn);
        btnGroup.add(blackBtn);
        colPanel.add(blackBtn);
        frame.add(colPanel,BorderLayout.WEST);

        //Radio Button
        frame.add(mouseBtn,BorderLayout.EAST);

        //Direction Panel
        JPanel dirPanel = new JPanel();
        dirPanel.add(btnLeft);
        dirPanel.add(btnRight);
        dirPanel.add(btnUp);
        dirPanel.add(btnDown);
        frame.add(dirPanel,BorderLayout.SOUTH);

        //Center Panel
        frame.add(this);

        this.setBackground(Color.WHITE);

    }

    

    
}


