import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class KeyboardEvent extends JPanel implements KeyListener{
    String text ="";
    KeyboardEvent(){
        addKeyListener(this);
        setFocusable(true);
    }


    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        g.setFont(new Font( "SansSerif", Font.BOLD, 30 ));
        g.drawString(text, 0, 100);

    }
    @Override
    public void keyTyped(KeyEvent e) {
        text +=  Character.toString(e.getKeyChar());
        repaint();
        
    }


    public void keyPressed(KeyEvent e) {}
    public void keyReleased(KeyEvent e) {}
    
}
