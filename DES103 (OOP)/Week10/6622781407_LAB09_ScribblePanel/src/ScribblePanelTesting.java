import javax.swing.JFrame;
import java.awt.BorderLayout;

public class ScribblePanelTesting {
    public static void main(String[] args){
        JFrame frame = new JFrame("Scribble Panel");
        ScribblePanel panel = new ScribblePanel();
        frame.setLayout(new BorderLayout());
        frame.add(panel, BorderLayout.CENTER); //add the object into CENTER of JFrame
        frame.setSize(300, 300); //set a frame's resolution
        frame.setLocationRelativeTo(null); //set a location at center the frame
        frame.setVisible(true); //set visible
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //set default Close Operation
    }
}
