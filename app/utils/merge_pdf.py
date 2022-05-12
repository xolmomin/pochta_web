import os
import fitz
region = 'yashnobod'
result = fitz.open()
list_pdfs = os.listdir(f'pochta_print/{region}')
list_pdfs.sort(key=lambda x: int(x))
# print(list_pdfs)
for pdf in list_pdfs:
    with fitz.open(f'pochta_print/{region}/{pdf}') as mfile:
        result.insert_pdf(mfile)

result.save(f'{region}.pdf')
