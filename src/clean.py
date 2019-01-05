#MODULO PARA LIMPIAR CONSOLA

def clean(var):
    if os.name == "posix":
        var = "clear"

    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"

    os.system(var)
