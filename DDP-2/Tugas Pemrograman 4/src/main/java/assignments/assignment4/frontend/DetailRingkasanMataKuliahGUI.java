package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

import assignments.assignment4.backend.*;

public class DetailRingkasanMataKuliahGUI {
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    public DetailRingkasanMataKuliahGUI(JFrame frame, MataKuliah mataKuliah, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah; 

        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));
        boxLayout.add(createText("Detail Ringkasan Mata Kuliah", 1));
        boxLayout.add(createText(String.format("Nama: %s", mataKuliah.getNama()), 0));
        boxLayout.add(createText(String.format("Kode: %s", mataKuliah.getKode()), 0));
        boxLayout.add(createText(String.format("SKS: %d", mataKuliah.getSKS()), 0));
        boxLayout.add(createText(String.format("Jumlah mahasiswa: %d", mataKuliah.getJumlahMahasiswa()), 0));
        boxLayout.add(createText(String.format("Kapasitas: %d", mataKuliah.getKapasitas()), 0));
        boxLayout.add(createText(String.format("Daftar Mahasiswa:"), 0));
        if (mataKuliah.getJumlahMahasiswa()!=0) {
            int counter =1;
            for (Mahasiswa mahasiswa : mataKuliah.getDaftarMahasiswa()) {
                if (mahasiswa!=null) {
                    boxLayout.add(createText(String.format("%d.%s",counter++,mahasiswa.getNama()), 0));
                }
            }
        }else{
            boxLayout.add(createText(String.format("Belum ada mata kuliah yang diambil"), 0));
        }
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

