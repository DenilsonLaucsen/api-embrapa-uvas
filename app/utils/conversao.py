def try_parse_int(valor: str) -> int:
    try:
        valor = valor.strip().replace(".", "").replace(",", "")
        return int(valor)
    except (ValueError, AttributeError):
        return 0
