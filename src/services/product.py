from flask import jsonify

from src.models.product import Product


""" Format products """


def format_products(dataRaw):
    products = []
    for item in dataRaw.items:
        product = format_product(item)
        products.append(product)
    return products


# Format product
def format_product(item):
    # print(item.options[0].color_data)
    option = {}
    if len(item.options) > 0:
        option["ram"] = item.options[0].ram
        option["rom"] = item.options[0].rom
        option["price"] = item.options[0].price
        option["image"] = item.options[0].image
        option["color_id"] = item.options[0].colorID
        option["color_value"] = item.options[0].color_data.value

    return {
        "id": item.id,
        "product_name": item.productName,
        "image": item.image,
        "cpu": item.cpu,
        "product_date": item.productDate,
        "origin": item.origin,
        "brandID": item.brandID,
        "brand_value": item.brand_data.value,
        "option": option,
    }


def get_all_products_service(data):
    try:
        # Get page
        page = data["page"] or "1"
        # get percent page. One page with per_page element
        per_page = data["per_page"] or "10"
        if not page.isdigit() or not per_page.isdigit():
            page = 1
            per_page = 10
        else:
            page = int(page)
            per_page = int(per_page)
        productRaw = Product.query.paginate(
            per_page=per_page, page=page, error_out=True
        )
        """Format data users"""
        products = format_products(productRaw)

        """Send data to client"""
        return jsonify(
            {
                "data": {
                    "products": products,
                    "per_page": productRaw.per_page,
                    "current_page": productRaw.page,
                    "total_pages": productRaw.pages,
                },
                "code": 0,
                "message": "Get all products success",
            }
        )
    except Exception as e:
        print("error here: ", e)
        return jsonify({"code": 2, "message": "Get all products fail"})
