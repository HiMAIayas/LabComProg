import javax.swing.JFrame;

public class KeyboardEventTesting {
    public static void main(String[] args) throws Exception {
        JFrame frame = new JFrame("My Keyboard Event");
        KeyboardEvent panel = new KeyboardEvent();
        frame.add(panel); //add add the object into the frame
        frame.setSize(800, 300); //set a frame's resolution
        frame.setLocationRelativeTo(null); //set a location at center the frame
        frame.setVisible(true); //set visible
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
