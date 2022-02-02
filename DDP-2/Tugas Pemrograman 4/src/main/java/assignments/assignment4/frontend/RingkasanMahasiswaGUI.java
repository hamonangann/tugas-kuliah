package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

import assignments.assignment4.backend.*;

public class RingkasanMahasiswaGUI {
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    protected JComboBox<Mahasiswa> npm ;
    public RingkasanMahasiswaGUI(JFrame frame, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah; 
        
        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));

        Mahasiswa[] daftaMahasiswa1 = daftarMahasiswa.toArray(new Mahasiswa[0]);
        this.npm = new JComboBox<Mahasiswa>(daftaMahasiswa1); //>.< kawaii
        npm.setSize(236,31);
        npm.setMaximumSize(npm.getSize());
        npm.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(createText("Ringkasan Mahasiswa", 1));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Pilih NPM", 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(npm);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Lihat",250, 207, 125));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Kembali",230, 146, 89));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        frame.add(boxLayout);
    }
    public JLabel createText(String name,int font) {
        JLabel titleLabel = new JLabel();
        titleLabel.setText(name);
        titleLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        titleLabel.setForeground(Color.white);
        switch (font) {
            case 1:titleLabel.setFont(SistemAkademikGUI.fontTitle);
                break;
            case 0:titleLabel.setFont(SistemAkademikGUI.fontGeneral);
                break;
        }
        return titleLabel;
    }
    public JButton createButton(String name, int R, int G , int B) {
        JButton button = new JButton(name);
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        button.setBackground(new Color(R,G,B));
        button.setForeground(Color.BLACK);

        switch (name) {
            case "Lihat": button.addActionListener(new ListenerRingkasanMahasiswa());break;
            case "Kembali": button.addActionListener(new ListenerKembali());break;
        }
        return button;
    }
    public class ListenerRingkasanMahasiswa implements ActionListener{
        public void actionPerformed(ActionEvent event){
            if (npm.getSelectedItem()==null) {
                JOptionPane.showMessageDialog(frame, String.format("Mohon isi seluruh field"));
                return;
            }
            Mahasiswa mahasiswa = getMahasiswa(Long.parseLong(npm.getSelectedItem().toString()));
            //String[] massalah = mahasiswa.getMasalahIRS();
            ringkasanMahasiswa(mahasiswa);
        }
    }
    public void ringkasanMahasiswa(Mahasiswa mahasiswa) {
        frame.getContentPane().removeAll();
        new DetailRingkasanMahasiswaGUI(frame, mahasiswa, daftarMahasiswa, daftarMataKuliah);
        frame.validate();
        frame.repaint();
    }
    public class ListenerKembali implements ActionListener{
        public void actionPerformed(ActionEvent event){
            frame.getContentPane().removeAll();
            new HomeGUI(frame, daftarMahasiswa, daftarMataKuliah);
            frame.validate();
            frame.repaint();
            
        }
        // TODO: Implementasikan Detail Ringkasan Mahasiswa
    }


    // Uncomment method di bawah jika diperlukan
    
    private Mahasiswa getMahasiswa(long npm) {

        for (Mahasiswa mahasiswa : daftarMahasiswa) {
            if (mahasiswa.getNpm() == npm){
                return mahasiswa;
            }
        }
        return null;
    }
    
}
