package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

import assignments.assignment4.backend.*;

public class TambahMataKuliahGUI{
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    protected JTextField kode = creaTextField();
    protected JTextField nama = creaTextField();
    protected JTextField sks =creaTextField();
    protected JTextField kapasitas =creaTextField();
    public TambahMataKuliahGUI(JFrame frame, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah;

        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));
        
        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(createText("Tambah Matakuliah", 1));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Kode Mata Kuliah:", 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(kode);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Nama Mata Kuliah:",0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(nama);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("SKS:",0));
        boxLayout.add(sks);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Kapasitas",0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(kapasitas);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Tambahkan",250, 207, 125));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Kembali",230, 146, 89));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        frame.add(boxLayout);
        // TODO: Implementasikan Tambah Mata Kuliah

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
            case "Tambahkan": button.addActionListener(new ListenerTambahMatkul());break;
            case "Kembali": button.addActionListener(new ListenerKembali());break;
        }
        return button;
    }

    public JTextField creaTextField() {
        JTextField input = new JTextField(50);
        input.setSize(236,31);
        input.setMaximumSize(input.getSize());
        input.setAlignmentX(Component.CENTER_ALIGNMENT);

        return input;
    }
    public class ListenerTambahMatkul implements ActionListener{
        public void actionPerformed(ActionEvent event){
            if (nama.getText().equals("") || sks.getText().equals("")||kapasitas.getText().equals("")||kode.getText().equals("")) {
                JOptionPane.showMessageDialog(frame, "Mohon isi seluruh Field");
                nama.setText("");
                sks.setText("");
                kapasitas.setText("");
                kode.setText("");
                return;
            }
            String name = nama.getText();
            int sks1 = Integer.parseInt(sks.getText());
            int kapasitas1 = Integer.parseInt(kapasitas.getText());
            String kode1 = kode.getText();
            if (getMataKuliah(name)==null) {
                daftarMataKuliah.add(new MataKuliah(kode1, name, sks1, kapasitas1));
                for(int i = 0; i < daftarMataKuliah.size()-1; i++){
                    int m = i;
                    for(int j = i + 1; j < daftarMataKuliah.size();j++){
                        if(daftarMataKuliah.get(m).getNama().compareToIgnoreCase(daftarMataKuliah.get(j).getNama()) > 0 ){
                            m = j;
                        }       
                    }
                    // Swapping elemen daftar Mata Kuliah
                    MataKuliah temp = daftarMataKuliah.get(i);
                    daftarMataKuliah.set(i, daftarMataKuliah.get(m));
                    daftarMataKuliah.set(m, temp);
                }
                JOptionPane.showMessageDialog(frame, String.format("Mata kuliah %s berhasil ditambahkan",name));
            }else{
                JOptionPane.showMessageDialog(frame, String.format("Mata kuliah %s sudah pernah ditambahkan sebelumnya",name));
            }
            nama.setText("");
            sks.setText("");
            kapasitas.setText("");
            kode.setText("");
            
        }
    }
    public MataKuliah getMataKuliah(String nama) {

        for (MataKuliah mataKuliah : daftarMataKuliah) {
            if (mataKuliah.getNama().equals(nama)){
                return mataKuliah;
            }
        }
        return null;
    }
    public class ListenerKembali implements ActionListener{
        public void actionPerformed(ActionEvent event){
            frame.getContentPane().removeAll();
            new HomeGUI(frame, daftarMahasiswa, daftarMataKuliah);
            frame.validate();
            frame.repaint();
            
        }
    }
    
}
