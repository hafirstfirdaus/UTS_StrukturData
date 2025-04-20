import csv

class Paper:
    def __init__(self, no, nim, namaMahasiswa, sumberDatabase, fokusKataKunci, title, year, author, abstractText, conclusion, link):
        self.no = no
        self.nim = nim
        self.namaMahasiswa = namaMahasiswa
        self.sumberDatabase = sumberDatabase
        self.fokusKataKunci = fokusKataKunci
        self.title = title
        self.year = year
        self.author = author
        self.abstractText = abstractText
        self.conclusion = conclusion
        self.link = link

def display_paper(p):
    """Menampilkan informasi jurnal secara rapi."""
    print("\n===========================================================")
    print(f"No               : {p.no}")
    print(f"NIM              : {p.nim}")
    print(f"Nama Mahasiswa   : {p.namaMahasiswa}")
    print(f"Sumber Database  : {p.sumberDatabase}")
    print(f"Fokus Kata Kunci : {p.fokusKataKunci}")
    print(f"Judul Paper      : {p.title}")
    print(f"Tahun Terbit     : {p.year}")
    print(f"Nama Penulis     : {p.author}")
    print(f"Abstrak          : {p.abstractText}")
    print(f"Kesimpulan       : {p.conclusion}")
    print(f"Link Paper       : {p.link}")
    print("===========================================================")

def linear_search(papers, keyword):
    """Melakukan pencarian linear berdasarkan nama mahasiswa."""
    result = [paper for paper in papers if keyword in paper.namaMahasiswa.lower()]
    return result

def binary_search(papers_sorted, keyword):
    """Melakukan pencarian binary berdasarkan nama mahasiswa (harus terurut)."""
    left, right = 0, len(papers_sorted) - 1
    results = []
    while left <= right:
        mid = (left + right) // 2
        mid_name = papers_sorted[mid].namaMahasiswa.lower()

        if keyword == mid_name:
            # Cari ke kiri dan kanan karena bisa ada lebih dari satu
            results.append(papers_sorted[mid])
            i = mid - 1
            while i >= 0 and papers_sorted[i].namaMahasiswa.lower() == keyword:
                results.append(papers_sorted[i])
                i -= 1
            i = mid + 1
            while i < len(papers_sorted) and papers_sorted[i].namaMahasiswa.lower() == keyword:
                results.append(papers_sorted[i])
                i += 1
            break
        elif keyword < mid_name:
            right = mid - 1
        else:
            left = mid + 1
    return results

def main():
    papers = []

    # Membaca file CSV
    try:
        with open("D:/UTS STRUDAT/Struktur_Data_Dataset_Kelas_A_B_C - Sheet1.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)  # Skip header

            for row in reader:
                if len(row) < 11:
                    print(f"Baris dilewati karena tidak lengkap: {row}")
                    continue
                no, nim, nama, sumber, fokus, title, year, author, abstrak, conclusion, link = row[:11]
                paper = Paper(no, nim, nama, sumber, fokus, title, year, author, abstrak, conclusion, link)
                papers.append(paper)

        print(f"Jumlah data yang berhasil dimuat: {len(papers)}")

    except FileNotFoundError:
        print("Gagal membuka file CSV. Pastikan file berada di direktori yang benar.")
        return

    # Membuat salinan dan mengurutkan untuk binary search
    papers_sorted = sorted(papers, key=lambda x: x.namaMahasiswa.lower())

    # Pencarian
    while True:
        mahasiswa_name = input("\nMasukkan nama mahasiswa yang ingin dicari (atau ketik 'exit' untuk keluar): ").strip().lower()
        if mahasiswa_name == "exit":
            print("Program selesai.")
            break

        search_method = input("Pilih metode pencarian - linear atau binary (ketik 'linear' / 'binary'): ").strip().lower()

        if search_method == "linear":
            mahasiswa_papers = linear_search(papers, mahasiswa_name)
        elif search_method == "binary":
            mahasiswa_papers = binary_search(papers_sorted, mahasiswa_name)
        else:
            print("Metode tidak dikenali. Coba lagi.")
            continue

        if not mahasiswa_papers:
            print("\nTidak ditemukan jurnal untuk mahasiswa tersebut.")
            continue

        print(f"\nDitemukan {len(mahasiswa_papers)} jurnal untuk mahasiswa '{mahasiswa_name}':")
        for i, paper in enumerate(mahasiswa_papers):
            print(f"{i + 1}. {paper.title} ({paper.year}) - {paper.author}")

        while True:
            search_term = input("\nMasukkan judul/tahun/penulis untuk mencari lebih spesifik (atau ketik 'back' untuk kembali): ").strip()
            if search_term.lower() == "back":
                break

            found = False
            for paper in mahasiswa_papers:
                if (search_term.lower() in paper.title.lower() or
                    search_term.lower() in paper.author.lower() or
                    search_term == str(paper.year)):
                    display_paper(paper)
                    found = True

            if not found:
                print("\nData tidak ditemukan.")

if __name__ == "__main__":
    main()
