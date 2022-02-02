package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.JOptionPane;
import javax.swing.plaf.ColorUIResource;

import java.util.ArrayList;

import assignments.assignment4.backend.*;


public class TambahMahasiswaGUI{
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    protected JTextField nama;
    protected JTextField npm;
    public TambahMahasiswaGUI(JFrame frame, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
        this.frame=frame;
        this.daftarMahasiswa=daftarMahasiswa;
        this.daftarMataKuliah=daftarMataKuliah;

        JPanel boxLayout = new JPanel();
        boxLayout.setLayout(new BoxLayout(boxLayout, BoxLayout.Y_AXIS));
        boxLayout.setBackground(new Color(33, 80, 61));
        nama = creaTextField();
        npm = creaTextField();

        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(createText("Tambah Mahasiswa", 1));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Nama:",0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(nama);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("NPM:",0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(npm);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Tambahkan",250, 207, 125));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Kembali",230, 146, 89));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        frame.add(boxLayout);
        // TODO: Implementasikan Tambah Mahasiswa

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

    public JTextField creaTextField() {
        JTextField input = new JTextField(50);
        input.setSize(236,31);
        input.setMaximumSize(input.getSize());
        input.setAlignmentX(Component.CENTER_ALIGNMENT);

        return input;
    }
    public JButton createButton(String name, int R, int G , int B) {
        JButton button = new JButton(name);
        button.setAlignmentX(Component.CENTER_ALIGNMENT);
        button.setBackground(new Color(R,G,B));
        button.setForeground(Color.BLACK);

        switch (name) {
            case "Tambahkan": button.addActionListener(new ListenerTambahMahasiswa());break;
            case "Kembali": button.addActionListener(new ListenerKembali());break;
        }
        return button;
    }
    public class ListenerTambahMahasiswa implements ActionListener{
        public void actionPerformed(ActionEvent event){
            if (nama.getText().equals("") || npm.getText().equals("")) {
                JOptionPane.showMessageDialog(frame, "Mohon isi seluruh Field");
                nama.setText("");
                npm.setText("");
                return;
            }
            String name = nama.getText();
            Long npm1 = Long.parseLong(npm.getText());
            if (getMahasiswa(npm1)==null) {
                daftarMahasiswa.add(new Mahasiswa(name, npm1));
                //loop untuk sorting
                for(int i = 0; i < daftarMahasiswa.size()-1; i++){
                    int m = i;
                    for(int j = i + 1; j < daftarMahasiswa.size(); j++){
                        if(daftarMahasiswa.get(m).getNpm() > daftarMahasiswa.get(j).getNpm()){
                            m = j;
                        }       
                    }
                // Swapping elemen daftar Mahasiswa
                    Mahasiswa temp = daftarMahasiswa.get(i);
                    daftarMahasiswa.set(i, daftarMahasiswa.get(m));
                    daftarMahasiswa.set(m, temp);
                }
                JOptionPane.showMessageDialog(frame, String.format("Mahasiswa %s-%s berhasil ditambahkan",npm.getText() ,nama.getText()));
            }else{
                JOptionPane.showMessageDialog(frame, String.format("NPM %s sudah pernah ditambahkan sebelumya",npm.getText() ,nama.getText()));
            }
            nama.setText("");
            npm.setText("");
        }
    }

    public class ListenerKembali implements ActionListener{
        public void actionPerformed(ActionEvent event){
            frame.getContentPane().removeAll();
            new HomeGUI(frame, daftarMahasiswa, daftarMataKuliah);
            frame.validate();
            frame.repaint();
            
        }
    }
    public Mahasiswa getMahasiswa(long npm) {

        for (Mahasiswa mahasiswa : daftarMahasiswa) {
            if (mahasiswa.getNpm() == npm){
                return mahasiswa;
            }
        }
        return null;
    }
}
