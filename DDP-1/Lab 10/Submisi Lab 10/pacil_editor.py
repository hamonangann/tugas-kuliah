from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.initUI()
        self.create_buttons()
        self.create_editor()

    def initUI(self):
        # TODO: Atur judul dan ukuran dari main window,
        # lalu buat sebuah Frame sebagai anchor dari seluruh button
        self.master.title("Pacil Editor")
        self.master.geometry("640x360")
        self.frame = Frame(self.master)
        self.frame.pack(side=TOP, anchor=NW)

    def create_buttons(self):
        # TODO: Implementasikan semua button yang dibutuhkan
        # Di baris teratas terdapat 3 button dari kiri ke kanan: Open File - Save File - Quit Program
        self.open = Button(self.frame, text="Open File", command=self.load_file)
        self.open.grid(row=0, column=0, padx=5, pady=5)
        self.save = Button(self.frame, text="Save File", command=self.save_file)
        self.save.grid(row=0, column=1, padx=5, pady=2)
        self.quit = Button(self.frame, text="Quit Program", command=self.master.destroy)
        self.quit.grid(row=0, column=2, padx=5, pady=2)
        pass

    def create_editor(self):
        # TODO: Implementasikan textbox
        # Textbox dapat menampung 78 karakter setiap baris, terletak di bawah button
        self.edit = Text(self.frame, width=78, height=20)
        self.edit.grid(row=1, column=0, columnspan=1000, padx=5, pady=5)
        pass
       
    def load_file_event(self, event):
        return self.load_file

    def load_file(self):
        file_name = askopenfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        text_file = open(file_name, 'r', encoding="utf-8")
        result = text_file.read()
        # TODO: tampilkan result di textbox
        self.set_text(result)

    def save_file_event(self, event):
       self.save_file

    def save_file(self):
        file_name = asksaveasfilename(
            filetypes=[("All files", "*")]
        )
        if not file_name:  # Jika pengguna membatalkan dialog, langsung return
            return
        # TODO: ambil isi dari textbox lalu simpan dalam file dengan nama file_name
        content = self.get_text()
        text_file = open(file_name, 'w', encoding="utf-8") # Membuat file baru atau mengosongkan file jika ada
        text_file.write(content) # Mengisi file dengan teks

    def set_text(self, text=''): # Mengisi textbox dengan teks dari file
        self.edit.delete('1.0', END)
        self.edit.insert('1.0', text)
        self.edit.mark_set(INSERT, '1.0')
        self.edit.focus()

    def get_text(self): # Menampung text dalam textbox
        return self.edit.get('1.0', END+'-1c')

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()