def describe_item(name: str, price: float, in_stock: bool = True) -> str:
    availability = "in stock" if in_stock else "out of stock"
    return f"{name} costs ${price} and is {availability}"

