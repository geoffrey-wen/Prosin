def displaytime(i, span):
    st = i*span
    fn = (i+1)*span
    sth = hour(st)
    fnh = hour(fn)
    stm = minute(st)
    fnm = minute(fn)
    disp = f"{sth}:{stm} - {fnh}:{fnm}"
    return disp


def hour(n):
    h = n//60
    if h < 10:
        p = f"0{h}"
    else:
        p = f"{h}"
    return p


def minute(n):
    m = n - (n//60)*60
    if m < 10:
        p = f"0{m}"
    else:
        p = f"{m}"
    return p