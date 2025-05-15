from use_cases.mahasiswa_usecase import MahasiswaUseCases
from infrastructure.in_memory_repo import InMemoryMahasiswaRepository

repo = InMemoryMahasiswaRepository()
usecase = MahasiswaUseCases(repo)

usecase.add("Budi", "Informatika")
usecase.add("Sari", "Teknik Sipil")

print("Semua Mahasiswa:", usecase.browse())
print("Data Mahasiswa ID 1:", usecase.read(1))
usecase.edit(1, "Budi Santoso", "Teknik Elektro")
print("Setelah Edit:", usecase.read(1))
usecase.delete(2)
print("Setelah Delete:", usecase.browse())
