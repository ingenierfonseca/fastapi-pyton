import math

def paginate(query, page: int, limit: int):
    skip = (page - 1) * limit
    total_items = query.count()
    total_pages = math.ceil(total_items / limit)
    items = query.offset(skip).limit(limit).all()
    return total_items, total_pages, items