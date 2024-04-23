import javax.swing.JFrame;

public class KeyboardGameTesting {
    public static void main(String[] args) {
        JFrame frame = new JFrame(); //create an object of this frame

        KeyboardGame panel = new KeyboardGame();
        frame.add(panel);
        //set a frame's resolution
        frame.setTitle("My Keyboard Game");
        frame.setSize(500, 300); //set a frame's resolution
        frame.setLocationRelativeTo(null); //set a location at center the frame
        frame.setVisible(true); //set visible
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //set default Close Operation
    }
}
