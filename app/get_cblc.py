import urllib.request
import struct

"""

"""


# source = 'http://127.0.0.1:8080/DBTCER9999.txt' # Debug with a local server
source = 'http://www.cblc.com.br/cblc/consultas/Arquivos/DBTCER9999.txt'
reg_size = 162  # (bytes) 160+linebreak+CR (from the official documentation)

data = urllib.request.urlopen(source)

# Total size in bytes is sent as a header
size = int(data.getheader('Content-Length'))
total_lines = int(size / reg_size)

# The first two bytes identify the registry kind
kind_mask = '2s'

# Each registry kind has its own struct mask, which will be used to parse byte
# objects by width. This approach makes it easy to change fields if needed.
registry_masks = [
    '2s6s4s8s4s8s8s120s',  # 00 = header
    '2s20s30s10s11s20s7s7s7s7s7s7s25s',  # 01 = one day
    '2s20s30s10s11s20s7s7s53s',  # 02 = three days
    '2s20s30s10s11s20s7s7s53s',  # 03 = fiften days
    '2s6s4s8s4s8s9s119s'  # 99 = trailer
]

# Pre-create the structs and then use them on specific functions to
# improve performance.
kind_struct = struct.Struct(kind_mask)

registry_00 = struct.Struct(registry_masks[0])
registry_01 = struct.Struct(registry_masks[1])
registry_02 = struct.Struct(registry_masks[2])
registry_03 = struct.Struct(registry_masks[3])
registry_99 = struct.Struct(registry_masks[4])


def parse_header(line):
    parsed = registry_00.unpack_from(line)
    parsed = [parsed.strip().decode() for parsed in parsed]
    keys = [
        'Tipo',
        'Codigo_arquivo',
        'Codigo_usuario',
        'Codigo_origem',
        'Codigo_destino',
        'Data_geracao',
        'Data_movimento',
        'Reserva'
        ]
    return dict(zip(keys, parsed))  # zip combines iterable elements


def parse_registry_one_day(line):
    parsed = registry_01.unpack_from(line)
    parsed = [parsed.strip().decode() for parsed in parsed]
    keys = [
        'Tipo',
        'Acao',
        'Empresa',
        'Num_Cont',
        'Qtd_Acao',
        'Valor',
        'Tx_Min_Doador',
        'Tx_Med_Doador',
        'Tx_Max_Doador',
        'Tx_Min_Tomador',
        'Tx_Med_Tomador',
        'Tx_Max_Tomador',
        'Reserva'
    ]
    return dict(zip(keys, parsed))


def parse_registry_three_days(line):
    parsed = registry_02.unpack_from(line)
    parsed = [parsed.strip().decode() for parsed in parsed]
    keys = [
        'Tipo',
        'Acao',
        'Empresa',
        'Num_Cont',
        'Qtd_Acao',
        'Valor',
        'Tx_Med_Doador',
        'Tx_Med_Tomador',
        'Reserva'
    ]
    return dict(zip(keys, parsed))


def parse_registry_fiften_days(line):
    parsed = registry_03.unpack_from(line)
    parsed = [parsed.strip().decode() for parsed in parsed]
    keys = [
        'Tipo',
        'Acao',
        'Empresa',
        'Num_Cont',
        'Qtd_Acao',
        'Valor',
        'Tx_Med_Doador',
        'Tx_Med_Tomador',
        'Reserva'
    ]
    return dict(zip(keys, parsed))


def parse_registry_trailer(line):
    parsed = registry_99.unpack_from(line)
    parsed = [parsed.strip().decode() for parsed in parsed]
    keys = [
        'Tipo',
        'Codigo_arquivo',
        'Codigo_usuario',
        'Codigo_origem',
        'Codigo_destino',
        'Data_geracao',
        'Qtd_registros',
        'Reserva'
    ]
    return dict(zip(keys, parsed))


# Pythonic way to perform a "case-switch" control is to use a dictionary
# to map functions.
parsers = {
    0: parse_header,
    1: parse_registry_one_day,
    2: parse_registry_three_days,
    3: parse_registry_fiften_days,
    99: parse_registry_trailer
}


def parse_registry(line):
    kind = int(kind_struct.unpack_from(line)[0].decode())
    parsed = parsers[kind](line)
    return parsed


with data as file:
    for line in range(0, total_lines):
        entry = file.read(reg_size)
        print(parse_registry(entry))
