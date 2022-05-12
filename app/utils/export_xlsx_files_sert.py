import os
import subprocess
import time

import fitz
import pandas as pd
from PIL import Image, ImageDraw, ImageFont, ImageOps
from barcode import EAN13
from barcode.writer import ImageWriter
from django.core.files.base import ContentFile
from docx import Document

from app.models import Letter


def _parse_to_doc_vars(xls_data):
    letter = Letter.objects.last()
    id_ = letter.id + 1
    name = xls_data[8] if len(xls_data[8].split()) < 3 else ' '.join(xls_data[8].split()[:2]) + '\n' + ' '.join(
        xls_data[8].split()[2:])
    result = {
        '{id_number}': f'{id_}'.zfill(12),
        '{region}': xls_data[0],
        '{address}': xls_data[6],
        '{account}': str(xls_data[5]),
        '{name}': name,
        '{date}': xls_data[7].strftime("%m/%d/%Y"),
    }
    return result


def _make_letter(doc_vars, client_id):
    file_url = f'app/template_pdf/cerf-shablon.docx'

    number = doc_vars['{id_number}']

    def _make_image_for_docx():
        img = Image.new('RGB', (900, 530), color=(255, 255, 255))

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("app/template_pdf/static/times.ttf", 48, encoding='UTF-8')
        region = 'г. Ташкент ' + doc_vars['{region}']
        address = doc_vars['{address}']
        account = 'Лицевой счет – ' + doc_vars['{account}']
        name = 'ФИО – ' + doc_vars['{name}']
        date = 'Срок госповерки ИПУГВ – ' + doc_vars['{date}']

        text = f'{number}\n{region}\n{address}\n{account}\n{name}\n{date}'

        draw.multiline_text((80, 180), text, font=font, align='center', fill='#000000')
        img = ImageOps.expand(img, border=2, fill='black')
        img.save(f'app/tmp/cerf/{number}_img.jpg')

    def _make_barcode():
        my_code = EAN13(number, writer=ImageWriter())
        my_code.save(f'app/tmp/cerf/{number}_barcode',
                     {'width': 0.1, 'height': 20, "module_width": 0.2, "module_height": 10, "write_text": False})

        im1 = Image.open(f'app/tmp/cerf/{number}_img.jpg')
        im2 = Image.open(f'app/tmp/cerf/{number}_barcode.png')
        back_im = im1.copy()
        back_im.paste(im2, (260, 50))
        back_im.save(f'app/tmp/cerf/{number}_img.jpg', quality=95)

    def _make_pdf_via_docx():
        doc = Document(file_url)
        for paragraph in doc.paragraphs:
            for item in doc_vars.keys():
                if item in paragraph.text:
                    inline = paragraph.runs
                    for i in range(len(inline)):
                        if item in inline[i].text:
                            text = inline[i].text.replace(item, doc_vars[item])
                            inline[i].text = text

        doc.save('app/tmp/cerf/result.docx')
        completed_docx_file = 'app/tmp/cerf/result.docx'
        subprocess.check_output(
            ['libreoffice', '--convert-to', 'pdf', completed_docx_file, '--outdir', 'app/tmp/cerf'])

    def _remove_file(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    def _remove_files():
        _remove_file(f'app/tmp/cerf/{number}_barcode.png')
        _remove_file(f'app/tmp/cerf/{number}_img.jpg')
        _remove_file(f'app/tmp/cerf/result.docx')
        _remove_file('app/tmp/cerf/result.pdf')
        _remove_file(f'app/tmp/cerf/{number}.pdf')

    def _merge_image_with_pdf():
        input_file = "app/tmp/cerf/result.pdf"
        output_file = f"app/tmp/cerf/{number}.pdf"
        barcode_file = f"app/tmp/cerf/{number}_img.jpg"

        image_rectangle = fitz.Rect(305, 20, 580, 245)

        file_handle = fitz.open(input_file)
        first_page = file_handle[0]

        first_page.insert_image(rect=image_rectangle, filename=barcode_file)
        file_handle.save(output_file)

    _make_image_for_docx()
    _make_barcode()
    _make_pdf_via_docx()
    _merge_image_with_pdf()

    letter = Letter.objects.create(
        client_id=client_id,
        address=doc_vars['{address}'],
        barcode=number,
    )

    file_path = f"app/tmp/cerf/{number}.pdf"
    fh = open(file_path, "rb")
    if fh:
        file_content = ContentFile(fh.read())
        letter.file.save(number, file_content)
        letter.save()

    fh.close()
    _remove_files()


# original_file_path = f'{qr_uuid}.png'
# qr = qrcode.make(full_url)
# qr.save(f'{media_path}/{original_file_path}')
# fh = open(f'{media_path}/{original_file_path}', "rb")
# if fh:
#     file_content = ContentFile(fh.read())
#     order.qr_code.save(f'{current_date}/{original_file_path}', file_content)
#     order.qr_uuid = qr_uuid
#     order.save()
#
# fh.close()


def generate_certification_pdf(file, client_id):  # TODO optimize
    df = pd.ExcelFile(file)
    start_total = time.time()

    for sheet_name in df.sheet_names:
        sheet_start_time = time.time()
        sheet_data = df.parse(sheet_name)
        for data in sheet_data.values:
            start_time = time.time()
            doc_var = _parse_to_doc_vars(data)
            _make_letter(doc_var, client_id)
            print("--- %s seconds each column ---" % (time.time() - start_time))
        print("--- %s seconds each sheet ---" % (time.time() - sheet_start_time))

    print("--- %s seconds ---" % (time.time() - start_total))
