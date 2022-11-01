# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

RLE_input_fn = 'RLE_input'
RLE_encoding_fn = 'RLE_encoding'
RLE_decoded_fn = 'RLE_decoded'


def getFileDetail(filename):
    import os
    file_details = os.stat(filename)
    result = file_details.st_size
    return result


def setRleEncode(data):
    encoding = ''
    value_previous = ''
    count = 1
    for value in data:
        if value != value_previous:
            if value_previous:
                encoding += str(count) + value_previous
            count = 1
            value_previous = value
        else:
            count += 1
    else:
        encoding += str(count) + value_previous

    with open(RLE_encoding_fn, 'w', encoding='UTF-8') as file:
        file.write(encoding)

    file_details = getFileDetail(RLE_encoding_fn)
    print(f'Размер сжатого файла: {file_details} байт')
    return encoding


def setRleDecode(data):
    decode = ''
    count = ''
    for value in data:
        if value.isdigit():
            count += value
        else:
            decode += value * int(count)
            count = ''
    with open(RLE_decoded_fn, 'w', encoding='UTF-8') as file:
        file.write(decode)

    file_details = getFileDetail(RLE_decoded_fn)
    print(f'Размер распакованного файла: {file_details} байт')
    return decode


RLE_input_file_details = getFileDetail(RLE_input_fn)
print(f'Размер исходного файла: {RLE_input_file_details} байт')

f_input = open(RLE_input_fn, 'r')
RLE_input = f_input.readline()
print(f'Исходные данные: \n{RLE_input}\n')
f_input.close()

RLE_encoded_file = setRleEncode(RLE_input)
print(f'Сжатые данные: {RLE_encoded_file}\n')

f_encode = open(RLE_encoding_fn, 'r')
RLE_encode = f_encode.readline()
f_encode.close()
RLE_decoded_file = setRleDecode(RLE_encode)
print(f'Распакованные данные: \n{RLE_decoded_file}')


input('\n\n\nНажмите "Enter ⏎" для выхода!')