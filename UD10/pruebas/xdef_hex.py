def hextonum(hex):
    pnum = { "f" : 15, "e" : 14, "d" : 13, "c" : 12, "b" : 11, "a" : 10}

    if hex in pnum:
        return pnum[hex]
    else:
        return int(hex)

def hextodec2(hex):
    hex = hex.lower()
    hex = hex[:: -1]
    decimal = 0
    posicio = 0
    for digit in hex:
        Valor = hextonum(digit)
        elevat = 16 ** posicio
        pnum = elevat * Valor
        decimal += pnum
        posicio += 1
    return decimal