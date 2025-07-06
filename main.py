import sys
import mysql.connector, requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem

class FormDisney(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('disney.ui', self)
        self.resize(900, 500)
        self.setMinimumSize(900, 500)
        
        self.init_db() 
        self.pushButton_cari.clicked.connect(self.cari_data)
        # self.pushButton_reset.clicked.connect(self.reset_data)
        self.pushButton_hapus.clicked.connect(self.hapus_data)
        # Saat baris dipilih, muat data ke form
        self.tableHistory.selectionModel().selectionChanged.connect(self.load_selected_row)
        self.tableHistory.setColumnHidden(0, True)
        self.view_data()


    def init_db(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost', user='root', password='', database='disney'
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Database Error', f'Gagal koneksi: {err}')
            sys.exit(1)

    def cari_data(self):
        input_nama = self.lineEdit_nama.text().strip().lower()
        input_film = self.lineEdit_films.text().strip().lower()
        input_tv = self.lineEdit_tvShow.text().strip().lower()
        input_game = self.lineEdit_vidGames.text().strip().lower()

        if not any([input_nama, input_film, input_tv, input_game]):
            QMessageBox.warning(self, 'Peringatan', 'Isi setidaknya satu field pencarian.')
            return

        try:
            response = requests.get(f'https://api.disneyapi.dev/character?name={input_nama}')
            response.raise_for_status()
            data = response.json()

            if not data['data']:
                QMessageBox.information(self, 'Tidak Ditemukan', 'Tidak ada karakter yang cocok.')
                return

            karakter_ditemukan = None
            for karakter in data['data']:
                karakter_films = [f.lower() for f in karakter.get('films', [])]
                karakter_tvs = [t.lower() for t in karakter.get('tvShows', [])]
                karakter_games = [g.lower() for g in karakter.get('videoGames', [])]

                if (
                    (not input_film or input_film in karakter_films) and
                    (not input_tv or input_tv in karakter_tvs) and
                    (not input_game or input_game in karakter_games)
                ):
                    karakter_ditemukan = karakter
                    break

            if not karakter_ditemukan:
                QMessageBox.information(self, 'Tidak Ditemukan', 'Tidak ada karakter yang cocok dengan semua input.')
                return

            # Ambil dan tampilkan data
            nama_karakter = karakter_ditemukan.get("name", "Tanpa nama")
            film = karakter_ditemukan.get("films", [''])[0] if karakter_ditemukan.get("films") else ''
            tv = karakter_ditemukan.get("tvShows", [''])[0] if karakter_ditemukan.get("tvShows") else ''
            game = karakter_ditemukan.get("videoGames", [''])[0] if karakter_ditemukan.get("videoGames") else ''

            self.lineEdit_nama.setText(nama_karakter)
            self.lineEdit_films.setText(film)
            self.lineEdit_tvShow.setText(tv)
            self.lineEdit_vidGames.setText(game)

            # Simpan ke DB
            self.cursor.execute(
                'INSERT INTO character_history (nama_char, film, tv_show, video_game) VALUES (%s, %s, %s, %s)',
                (nama_karakter, film, tv, game)
            )
            self.conn.commit()

            QMessageBox.information(self, 'Sukses', f'Karakter "{nama_karakter}" berhasil disimpan.')
            self.clear_fields()
            self.view_data()

        except requests.exceptions.RequestException as api_err:
            QMessageBox.critical(self, 'Error API', f'Gagal ambil data dari API: {api_err}')
        except mysql.connector.Error as db_err:
            QMessageBox.critical(self, 'Error DB', f'Gagal simpan ke database: {db_err}')

    
    
    def load_selected_row(self):
        row = self.tableHistory.currentRow()
        if row >= 0:
            self.lineEdit_nama.setText(self.tableHistory.item(row, 1).text())
            self.lineEdit_films.setText(self.tableHistory.item(row, 2).text())
            self.lineEdit_tvShow.setText(self.tableHistory.item(row, 3).text())
            self.lineEdit_vidGames.setText(self.tableHistory.item(row, 4).text())


    def hapus_data(self):
        row = self.tableHistory.currentRow()
        if row < 0:
            QMessageBox.warning(self, 'Peringatan', 'Pilih baris untuk dihapus!')
            return
        record_id = int(self.tableHistory.item(row, 0).text())
        confirm = QMessageBox.question(
            self, 'Konfirmasi', 'Yakin ingin menghapus data ini?',
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return
        try:
            self.cursor.execute('DELETE FROM character_history WHERE id=%s', (record_id,))
            self.conn.commit()
            QMessageBox.information(self, 'Sukses', 'Data berhasil dihapus.')
            self.clear_fields()
            self.view_data()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Error', f'Gagal hapus: {err}')
    
    def view_data(self):
        self.cursor.execute('SELECT id, nama_char, film, tv_show, video_game FROM character_history ORDER BY id DESC')
        rows = self.cursor.fetchall()

        self.tableHistory.setColumnCount(5)
        self.tableHistory.setHorizontalHeaderLabels(['ID', 'Nama', 'Film', 'TV Show', 'Game'])
        self.tableHistory.setRowCount(len(rows))

        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableHistory.setItem(i, j, QTableWidgetItem(str(val)))


    def clear_fields(self):
        self.lineEdit_nama.clear()
        self.lineEdit_films.clear()
        self.lineEdit_tvShow.clear()
        self.lineEdit_vidGames.clear()
        self.tableHistory.clearSelection()


    def closeEvent(self, event):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
        event.accept()

if __name__ == '__main__':
    # pip install mysql-connector-python
    app = QApplication(sys.argv)
    window = FormDisney()
    window.show()
    sys.exit(app.exec_())