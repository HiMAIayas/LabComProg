import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;

public class KeyboardGame extends JPanel implements ActionListener, KeyListener{
    char alp = 'Z';
    char alp_ans = '?';
    int score = 0;
    boolean isTyped = false;

    Color sec_color = Color.BLUE;

    Font font = new Font("Sanserif",Font.BOLD,45);
    Timer timer = new Timer(1000,this);
    KeyboardGame(){
        timer.start();
        this.addKeyListener(this);
        this.setFocusable(true);
    }
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        g.setFont(font);
        g.drawString("Letter: "+alp, 75, 75);
        g.drawString("You typed ", 75, 150);
        g.drawString("Score = "+score, 75, 225);

        g.setColor(sec_color);
        g.drawString(String.valueOf(alp_ans), 350, 150);
    }
    @Override
    public void actionPerformed(ActionEvent e) {
        alp = (char)(65+new Random().nextInt(26));
        
        isTyped = false;
        sec_color = Color.BLUE;
        repaint();
    }

    @Override
    public void keyTyped(KeyEvent e) {
        if (!isTyped){
            System.out.println(e.getKeyChar());
            alp_ans = e.getKeyChar();

            if (alp==alp_ans){
                sec_color = Color.GREEN;
                isTyped = true;
                score+=1;
                repaint();
            }
            else {
                sec_color = Color.RED;
                repaint();
            }
        }

        
    }

    public void keyPressed(KeyEvent e) {}
    public void keyReleased(KeyEvent e) {}
}
