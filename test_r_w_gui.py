
import csv
import tkinter as tk

# 文字フォントを設定
font1 = ("Meiryo",10)
font2 = ("Meiryo",8)

# csvのファイルパス
filepath = "D:/VScode_lesson/limbus_coin_sim/test/data.csv"


class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master,
            padx= 10,
            pady= 10,
        )

        # csvを読み込む処理
        with open(filepath, newline= "", encoding= "utf-8_sig") as cf:
            reader = csv.reader(cf)
            # リストボックスに追加する初期値
            data = list(reader)

        self.make_widget()
        self.init_listbox(data)


    def make_widget(self):
        # エントリー
        self.entry = tk.Entry(self,
            width= 20,
            font= font1,
        )
        self.entry.grid(row= 0, column= 0,
            columnspan= 3,
            padx= 5, pady= 5,
        )

        # 書き込みボタン
        w_button = tk.Button(self,
            width= 4,
            text= "wirte", font= font1,
            justify= tk.CENTER,
            command= self.write,
        )
        w_button.grid(row= 1, column= 0,
            columnspan= 1,
            padx= 5, pady= 5,
        )

        # 読み込みボタン
        r_button = tk.Button(self,
            width= 4,
            text= "read", font= font1,
            justify= tk.CENTER,
            command= self.read,
        )
        r_button.grid(row= 1, column= 1,
            columnspan= 1,
            padx= 5, pady= 5,
        )

        # 削除ボタン
        d_button = tk.Button(self,
            width= 4,
            text= "delete", font= font1,
            justify= tk.CENTER,
            command= self.delete,
        )
        d_button.grid(row= 1, column= 2,
            columnspan= 1,
            padx= 5, pady= 5,
        )

        # リストボックス
        self.listbox = tk.Listbox(self,
            font= font2,
            width= 40, height= 15,
            selectmode= "single",
        )
        self.listbox.grid(row= 2, column= 0,
            columnspan= 3,
            padx= 5, pady= 5,
        )


    def init_listbox(self, data:list[list[str]]):
        for value in data:
            self.listbox.insert(tk.END, value[0])


    def write(self):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.listbox.insert(tk.END,text)


    def read(self):
        # 選択されている項目のインデックスを取得
        indexes = self.listbox.curselection()
        # curselectionを使うと選択した項目のインデックスをタプルとして取得する
        if len(indexes) != 1:
            # タプルの項目数が1以外
            return

        self.entry.delete(0, tk.END)
        # indexesがタプルなので[0]を付けてインデックスを取得する
        text = self.listbox.get(indexes[0])
        self.entry.insert(0, text)


    def delete(self):
        indexes = self.listbox.curselection()
        if len(indexes) != 1:
            return

        self.listbox.delete(indexes[0])




class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("test")
        # self.geometry("400x500")
        self.protocol("WM_DELETE_WINDOW",self.on_closing)

        self.frame = MainFrame(self)
        self.frame.pack()

    def on_closing(self):
        self.write_csv()
        self.destroy()

    def write_csv(self):
        # タプルとしてデータが得られる
        data = self.frame.listbox.get(0, self.frame.listbox.size())

        # 二次元配列へ変換
        data = [ [value] for value in data ]

        with open(filepath, mode= "w", newline= "", encoding= "utf-8_sig") as cf:
            writer = csv.writer(cf)
            writer.writerows(data)


if __name__ == "__main__":
    App().mainloop()
