package assignments.assignment4.frontend;

import javax.swing.JFrame;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

import assignments.assignment4.backend.*;

public class HomeGUI {
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    public HomeGUI(JFrame frame, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah; 
        
        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));
        ImageIcon imageIcon = new ImageIcon(new ImageIcon("assignment4/kampus-ui.jpg").getImage().getScaledInstance(120, 120, Image.SCALE_SMOOTH));
        JLabel img = new JLabel(imageIcon);
        JLabel titleLabel = new JLabel();
        titleLabel.setText("Selamat datang di Sistem Akademik");
        titleLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        titleLabel.setFont(SistemAkademikGUI.fontTitle);
        titleLabel.setForeground(Color.white);

        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(titleLabel);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Tambah Mahasiswa"));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Tambah Mata Kuliah"));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Tambah IRS"));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Hapus IRS"));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Lihat Ringkasan Mahasiswa"));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Lihat Ringkasan Matakuliah"));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(img);
        frame.add(boxLayout);
        // TODO: Implementasikan Halaman Home
    }

    public JButton createButton(String name) {
        JButton button = new JButton(name);
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        button.setBackground(new Color(230, 146, 89));
        button.setForeground(Color.BLACK);

        switch (name) {
            case "Tambah Mahasiswa": button.addActionListener(new ListenerTambahMahasiswa());break;
            case "Tambah Mata Kuliah": button.addActionListener(new ListenerTambahMataKuliah());break;
            case "Tambah IRS": button.addActionListener(new ListenerTambahIRS());break;
            case "Hapus IRS": button.addActionListener(new ListenerHapusIRS());break;
            case "Lihat Ringkasan Mahasiswa": button.addActionListener(new ListenerRingkasanMahasiswa());break;
            case "Lihat Ringkasan Matakuliah": button.addActionListener(new ListenerRingkasanMataKuliah());break;
        }
        return button;
    }
    public void clearFrame(String name) {
        frame.getContentPane().removeAll();
        switch (name) {
            case "Tambah Mahasiswa": new TambahMahasiswaGUI(frame, daftarMahasiswa, daftarMataKuliah);
                break;
            case "Tambah Mata Kuliah": new TambahMataKuliahGUI(frame, daftarMahasiswa, daftarMataKuliah);
                break;
            case "Tambah IRS": new TambahIRSGUI(frame, daftarMahasiswa, daftarMataKuliah);
                break;
            case "Hapus IRS": new HapusIRSGUI(frame, daftarMahasiswa, daftarMataKuliah);
                break;
            case "Lihat Ringkasan Mahasiswa": new RingkasanMahasiswaGUI(frame, daftarMahasiswa, daftarMataKuliah);
                break;
            case "Lihat Ringkasan Mata Kuliah": new RingkasanMataKuliahGUI(frame, daftarMahasiswa, daftarMataKuliah);
                break;
        }
        frame.validate();
        frame.repaint();
    }
    public class ListenerTambahMahasiswa implements ActionListener{
        public void actionPerformed(ActionEvent event){
            clearFrame("Tambah Mahasiswa");
            
        }
    }
    public class ListenerTambahMataKuliah implements ActionListener{
        public void actionPerformed(ActionEvent event){
            clearFrame("Tambah Mata Kuliah");
            
        }
    }
    public class ListenerTambahIRS implements ActionListener{
        public void actionPerformed(ActionEvent event){
            clearFrame("Tambah IRS");
            
        }
    }
    public class ListenerHapusIRS implements ActionListener{
        public void actionPerformed(ActionEvent event){
            clearFrame("Hapus IRS");
            
        }
    }
    public class ListenerRingkasanMahasiswa implements ActionListener{
        public void actionPerformed(ActionEvent event){
            clearFrame("Lihat Ringkasan Mahasiswa");
            
        }
    }
    public class ListenerRingkasanMataKuliah implements ActionListener{
        public void actionPerformed(ActionEvent event){
            clearFrame("Lihat Ringkasan Mata Kuliah");
            
        }
    }

}
