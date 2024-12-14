import os
from PyPDF2 import PdfMerger

# PDF dosyalarını birleştirecek bir PdfMerger nesnesi oluşturuyoruz
merger = PdfMerger()

# Belirtilen dizindeki PDF dosyalarını almak
directory = r"C:\Users\denem\Documents\lesson\konular\Aı"

# Dizin içindeki PDF dosyalarını alıyoruz
pdf_files = [f for f in os.listdir(directory) if f.endswith('.pdf')]

# Dosya adlarını sıralı bir şekilde almak için, dosyadaki hafta numarasına göre sıralama yapıyoruz
pdf_files.sort(key=lambda x: int(x.split(' - ')[-1].split('.')[0]))

# PDF dosyalarını sırasıyla ekliyoruz
for pdf in pdf_files:
    pdf_path = os.path.join(directory, pdf)
    merger.append(pdf_path)

# Sonuçları birleştirilmiş olarak kaydediyoruz
output_file = os.path.join(directory, "combined.pdf")
merger.write(output_file)
merger.close()

print(f"PDF dosyaları başarıyla birleştirildi: {output_file}")
