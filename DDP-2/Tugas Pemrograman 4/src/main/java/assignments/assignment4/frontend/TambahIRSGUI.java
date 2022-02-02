package assignments.assignment4.frontend;

import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
 

import assignments.assignment4.backend.*;

public class TambahIRSGUI {
    protected JFrame frame;
    protected ArrayList<Mahasiswa> daftarMahasiswa;
    protected ArrayList<MataKuliah> daftarMataKuliah;
    protected JComboBox<MataKuliah> matkul;
    protected JComboBox<Mahasiswa> npm ;
    public TambahIRSGUI(JFrame frame, ArrayList<Mahasiswa> daftarMahasiswa, ArrayList<MataKuliah> daftarMataKuliah){
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

        MataKuliah[] daftarMataKuliah1 = daftarMataKuliah.toArray(new MataKuliah[0]);
        this.matkul = new JComboBox<MataKuliah>(daftarMataKuliah1);
        matkul.setSize(236,31);
        matkul.setMaximumSize(matkul.getSize());
        matkul.setAlignmentX(Component.CENTER_ALIGNMENT);


        boxLayout.add(Box.createRigidArea(new Dimension(65,65)));
        boxLayout.add(createText("Tambah IRS", 1));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Pilih NPM", 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(npm);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createText("Pilih Nama Maktul", 0));
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(matkul);
        boxLayout.add(Box.createRigidArea(new Dimension(5,5)));
        boxLayout.add(createButton("Tambahkan",250, 207, 125));
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
            case "Tambahkan": button.addActionListener(new ListenerTambahIRS());break;
            case "Kembali": button.addActionListener(new ListenerKembali());break;
        }
        return button;
    }
    public class ListenerTambahIRS implements ActionListener{
        public void actionPerformed(ActionEvent event){
            if (npm.getSelectedItem() == null||matkul.getSelectedItem() == null) {
                JOptionPane.showMessageDialog(frame, String.format("Mohon isi seluruh field"));
                return;
            }
            Mahasiswa mahasiswa = getMahasiswa(Long.parseLong(npm.getSelectedItem().toString()));
            MataKuliah mataKuliah = getMataKuliah(matkul.getSelectedItem().toString());
            String cek =mahasiswa.addMatkul(mataKuliah);
            if (cek.substring(0, 9).equals("[BERHASIL]")) {
                mataKuliah.addMahasiswa(mahasiswa);
                JOptionPane.showMessageDialog(frame, String.format(cek));
            }else{
                JOptionPane.showMessageDialog(frame, cek);
            }
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
    // Uncomment method di bawah jika diperlukan
    
    private MataKuliah getMataKuliah(String nama) {

        for (MataKuliah mataKuliah : daftarMataKuliah) {
            if (mataKuliah.getNama().equals(nama)){
                return mataKuliah;
            }
        }
        return null;
    }

    private Mahasiswa getMahasiswa(long npm) {

        for (Mahasiswa mahasiswa : daftarMahasiswa) {
            if (mahasiswa.getNpm() == npm){
                return mahasiswa;
            }
        }
        return null;
    }
    
}
