def filter_customers(customers: list, query: str) -> list:
    """
    Filtra la lista de clientes basándose en el query.
    Lanza ValueError si el término es menor a 3 caracteres.
    Retorna la lista de clientes que coinciden con query en name o email (case-insensitive).
    """
    if query is None or len(query) < 3:
        raise ValueError("Search term must be at least 3 characters long.")

    q_lower = query.lower()
    return [
        customer
        for customer in customers
        if q_lower in customer.get("name", "").lower()
        or q_lower in customer.get("email", "").lower()
    ]