package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

import assignments.assignment4.backend.*;

public class RingkasanMataKuliahGUI {
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    JComboBox<MataKuliah> matakuliah;
    public RingkasanMataKuliahGUI(JFrame frame, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah; 

        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));

        MataKuliah[] daftaMataKuliah1 = daftarMataKuliah.toArray(new MataKuliah[0]);
        this.matakuliah = new JComboBox<MataKuliah>(daftaMataKuliah1); //>.< kawaii
        matakuliah.setSize(236,31);
        matakuliah.setMaximumSize(matakuliah.getSize());
        matakuliah.setAlignmentX(Component.CENTER_ALIGNMENT);
        
        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(createText("Ringkasan Mata Kuliah", 1));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Pilih Nama Matkul", 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(matakuliah);
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
            if (matakuliah.getSelectedItem()==null) {
                JOptionPane.showMessageDialog(frame, String.format("Mohon isi seluruh field"));
                return;
            }
            MataKuliah matkul = getMataKuliah(matakuliah.getSelectedItem().toString());
            ringkasanMatkul(matkul);
        }
    }
    public void ringkasanMatkul(MataKuliah matkul) {
        frame.getContentPane().removeAll();
        new DetailRingkasanMataKuliahGUI(frame, matkul, daftarMahasiswa, daftarMataKuliah);
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
    }

    // Uncomment method di bawah jika diperlukan
    
    private MataKuliah getMataKuliah(String nama) {

        for (MataKuliah mataKuliah : daftarMataKuliah) {
            if (mataKuliah.getNama().equals(nama)){
                return mataKuliah;
            }
        }
        return null;
    }
    
}
