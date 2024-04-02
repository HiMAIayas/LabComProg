import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

import javax.swing.JPanel;

public class ScribblePanel extends JPanel implements MouseMotionListener, MouseListener{
    int X; int Y;
    boolean leftClick;
    boolean rightClick;
    ScribblePanel(){
        this.addMouseListener(this);
        this.addMouseMotionListener(this);
    }


    @Override
    public void mouseDragged(MouseEvent e) {
        Graphics g = getGraphics();
        if (leftClick){
            g.drawLine(X, Y, e.getX(), e.getY());
            X=e.getX();
            Y=e.getY();
        }
        else{

            g.setColor(getBackground());
            g.fillRect(X, Y, e.getX()-X, e.getY()-Y);
        }
    }

    
    @Override
    public void mousePressed(MouseEvent e) {
        X=e.getX();
        Y=e.getY();
        if(e.getButton()==MouseEvent.BUTTON1) {
            leftClick=true;
            rightClick=false;
        }
        else if (e.getButton()==MouseEvent.BUTTON3){
            leftClick=false;
            rightClick=true;
        }
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        Graphics g = getGraphics();
        if (rightClick){
            g.setColor(getBackground());
            g.fillRect(X, Y, e.getX()-X, e.getX()-Y);
        }
    }

    public void mouseMoved(MouseEvent e) {}
    public void mouseClicked(MouseEvent e) {}
    public void mouseEntered(MouseEvent e) {}
    public void mouseExited(MouseEvent e) {}
}
