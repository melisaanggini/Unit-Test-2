from use_cases.mahasiswa_usecase import MahasiswaUseCases
from infrastructure.in_memory_repo import InMemoryMahasiswaRepository

def menu(usecase):
    while True:
        print("\n1. Tambah Mahasiswa\n2. Lihat Semua Mahasiswa\n3. Cari Mahasiswa berdasarkan ID\n4. Ubah Data Mahasiswa\n5. Hapus Mahasiswa\n6. Keluar")
        choice = input("Pilih: ")
        
        if choice == "1":
            nama = input("Nama Mahasiswa: ")
            jurusan = input("Jurusan: ")
            usecase.add(nama, jurusan)
            print(f"Mahasiswa {nama} berhasil ditambahkan.")
        
        elif choice == "2":
            mahasiswa_list = usecase.browse()
            for m in mahasiswa_list:
                print(f"{m.id}: {m.nama} - {m.jurusan}")
        
        elif choice == "3":
            id_mahasiswa = int(input("ID Mahasiswa: "))
            mahasiswa = usecase.read(id_mahasiswa)
            if mahasiswa:
                print(f"{mahasiswa.id}: {mahasiswa.nama} - {mahasiswa.jurusan}")
            else:
                print("Mahasiswa tidak ditemukan.")
        
        elif choice == "4":
            id_mahasiswa = int(input("ID Mahasiswa yang ingin diubah: "))
            nama_baru = input("Nama baru: ")
            jurusan_baru = input("Jurusan baru: ")
            mahasiswa = usecase.edit(id_mahasiswa, nama_baru, jurusan_baru)
            if mahasiswa:
                print(f"Mahasiswa dengan ID {id_mahasiswa} berhasil diubah.")
            else:
                print("Mahasiswa tidak ditemukan.")
        
        elif choice == "5":
            id_mahasiswa = int(input("ID Mahasiswa yang ingin dihapus: "))
            success = usecase.delete(id_mahasiswa)
            if success:
                print(f"Mahasiswa dengan ID {id_mahasiswa} berhasil dihapus.")
            else:
                print("Mahasiswa tidak ditemukan.")
        
        elif choice == "6":
            break

if __name__ == "__main__":
    repo = InMemoryMahasiswaRepository()
    usecase = MahasiswaUseCases(repo)

    # Contoh data awal
    usecase.add("Budi", "Informatika")
    usecase.add("Sari", "Teknik Sipil")

    menu(usecase)
