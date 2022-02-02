import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class CounterFrame extends JFrame {

    // Declaring the variables
    private JPanel panelNorth;
    private JPanel panelEast;
    private JPanel panelWest;
    private JPanel panelSouth;
    private JPanel panelCenter;
    private JLabel titleLabel;
    private JLabel counterLabel;
    private JButton plusButton;
    private JButton minusButton;
    private JButton resetButton;
    private int count;
    

    public CounterFrame(){

        // TODO : Fill in the blanks
        // Frame title: "The Counter GUI"
        this.setTitle("The Counter GUI"); //sets title of frame
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //exit out of appliaction
        this.setResizable(true); //makes the frame resizeable
        this.setSize(500, 500); //sets the x-dimension and y-dimension of frame

        // Initializing the JPanels
        panelNorth = new JPanel();
        panelEast = new JPanel();
        panelWest = new JPanel();
        panelSouth = new JPanel();
        panelCenter = new JPanel();

        // Using the BorderLayout for the Frame and Center, East, and West Panel
        this.setLayout(new BorderLayout());
        panelCenter.setLayout(new BorderLayout());
        panelEast.setLayout(new BorderLayout());
        panelWest.setLayout(new BorderLayout());

        // Feel free to customize these colors
        panelNorth.setBackground(Color.CYAN);
        panelCenter.setBackground(Color.GRAY);
        panelSouth.setBackground(Color.CYAN);

        // Initializing and setting the titleLabel
        // TODO : Fill in the blanks
        titleLabel = new JLabel();
        titleLabel.setText("The Counter"); // Title lable on north
        titleLabel.setHorizontalAlignment(JLabel.CENTER);
        titleLabel.setFont(new Font("Courier New", Font.BOLD, 50)); // Feel free to customize the font


        // Initializing and setting the counterLabel
        // TODO : Fill in the blanks
        counterLabel = new JLabel();
        counterLabel.setText(String.valueOf(count)); // Clue : use the 'count' variable ->convert to string
        counterLabel.setHorizontalAlignment(JLabel.CENTER);
        counterLabel.setVerticalAlignment(JLabel.CENTER);
        counterLabel.setFont(new Font("Serif", Font.PLAIN, 50)); // Feel free to customize the font

        // Initializing the JButtons
        // TODO : Fill in the blanks
        plusButton = new JButton("+");
        minusButton = new JButton("-");
        resetButton = new JButton("RESET");

        plusButton.setFont(new Font("Courier New", Font.PLAIN, 50)); // Feel free to customize the font
        plusButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                // TODO : Increment the counter
                counterLabel.setText(String.valueOf(++count)); // Increment before print the text
            }
        });

        minusButton.setFont(new Font("Courier New", Font.PLAIN, 50)); // Feel free to customize the font
        minusButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                // TODO : Decrement the counter
                if (count > 0) counterLabel.setText(String.valueOf(--count)); // Decrement before print
            }
        });

        resetButton.setFont(new Font("Courier New", Font.PLAIN, 25)); // Feel free to customize the font
        resetButton.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e){
                // TODO : Reset the counter
                counterLabel.setText("0"); // Default value
            }     
        });

        // TODO : Add the right labels and titles to the corresponding panel
        panelNorth.add(titleLabel);
        panelEast.add(plusButton);
        panelWest.add(minusButton);
        panelSouth.add(resetButton);
        panelCenter.add(counterLabel);

        // TODO : Add the right panels into the right layout position
        this.add(panelNorth, BorderLayout.NORTH);
        this.add(panelEast, BorderLayout.EAST);
        this.add(panelWest, BorderLayout.WEST);
        this.add(panelSouth, BorderLayout.SOUTH);
        this.add(panelCenter, BorderLayout.CENTER);

        this.setVisible(true); // Making the frame visible
    }
}
