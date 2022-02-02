package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

import assignments.assignment4.backend.*;

public class DetailRingkasanMahasiswaGUI {
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    public DetailRingkasanMahasiswaGUI(JFrame frame, Mahasiswa mahasiswa, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah; 

        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));
        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(createText("Detail Ringkasan Mahasiswa", 1));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText(String.format("Nama: %s", mahasiswa.getNama()), 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText(String.format("Jurusan: %s", mahasiswa.getJurusan()), 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText(String.format("NPM: %d", mahasiswa.getNpm()), 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText(String.format("Daftar Mata Kuliah:"), 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        if (mahasiswa.getBanyakMatkul()!=0) {
            int counter =1;
            for (MataKuliah mataKuliah : mahasiswa.getMataKuliah()) {
                if (mataKuliah!=null) {
                    boxLayout.add(createText(String.format("%d.%s",counter++,mataKuliah.toString()), 0));
                }
            }
        }else{
            boxLayout.add(createText(String.format("Belum ada mata kuliah yang diambil"), 0));
        }
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText(String.format("Total SKS: %d",mahasiswa.getTotalSKS()), 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText(String.format("Hasil pengecekan IRS:"), 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        mahasiswa.cekIRS();
        if (mahasiswa.getMasalahIRS()[0]!=null) {
            int counter =1;
            for (String masalah: mahasiswa.getMasalahIRS()) {
                if (masalah!=null) {
                    boxLayout.add(createText(String.format("%d.%s",counter++,masalah), 0,229, 89, 87));
                }
            }
        }else{
            boxLayout.add(createText(String.format("IRS tidak bermasalah"), 0));
        }
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Selesai", 230, 146, 89));

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
    public JLabel createText(String name,int font, int R, int G, int B) {
        JLabel titleLabel = new JLabel();
        titleLabel.setText(name);
        titleLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        titleLabel.setForeground(new Color(R,G,B));
        titleLabel.setFont(new Font("Century Gothic", Font.BOLD, 14));
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
            case "Selesai": button.addActionListener(new ListenerSelesai());break;
        }
        return button;
    }
    public class ListenerSelesai implements ActionListener{
        public void actionPerformed(ActionEvent event){
            frame.getContentPane().removeAll();
            new RingkasanMahasiswaGUI(frame, daftarMahasiswa, daftarMataKuliah);
            frame.validate();
            frame.repaint();
            
        }
        // TODO: Implementasikan Detail Ringkasan Mahasiswa
    }
}
