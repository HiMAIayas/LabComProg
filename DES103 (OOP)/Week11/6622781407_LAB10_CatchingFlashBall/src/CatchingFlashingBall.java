import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.Random;
import javax.swing.*;

public class CatchingFlashingBall extends JPanel{

    int X = 0;
    int Y = 0;
    Timer timer = new Timer(500,new TimerListener());
    int radius = 10;

    CatchingFlashingBall(){

        this.setBackground(Color.BLACK);
        this.addMouseListener(new Catcher());
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.ORANGE);
        g.fillOval(X-radius, Y-radius, 2*radius, 2*radius);
    }


    class TimerListener implements ActionListener{

        @Override
        public void actionPerformed(ActionEvent e) {
            Random rand = new Random();
            X = radius+rand.nextInt(getWidth()-radius);
            Y = radius+rand.nextInt(getHeight()-radius);
            repaint();
            }

    }

    class Catcher implements MouseListener{
        @Override
        public void mousePressed(MouseEvent e) {
            if (calculateDistance(X, Y, e.getX(), e.getY())<=radius){
                timer.stop();
            }
        }


        public void mouseReleased(MouseEvent e) {}
        public void mouseClicked(MouseEvent e) {}
        public void mouseEntered(MouseEvent e) {}
        public void mouseExited(MouseEvent e) {}

        double calculateDistance(int x1, int y1, int x2, int y2) {
            return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
        }
        
    }
}
