def menu_option_entity(menu) -> dict:
    return {
        'id': str(menu['_id']),
        'name': menu['name'],
        'restaurant': str(menu['restaurant']),
        'products': [
            {
                'product' : str(product['_id']),
                'quantity': product['quantity']
            } for product in menu['products']
        ],
        'price': menu['price'],
        'type': menu['type'],
        'status': menu['status']
    }

def menu_options_entity(entity) -> list:
    return [menu_option_entity(item) for item in entity]

menu_option_pipeline = [
    {
        "$match": {
            "status": "active"
        }
    },
    {
        "$lookup": {
            "from": "products",
            "localField": "products.product",
            "foreignField": "_id",
            "as": "products_info"
        }
    },
    {
        "$project": {
            "_id": 1,
            "name": 1,
            "restaurant": 1,
            "products": {
                "$map": {
                    "input": "$products",
                    "as": "product",
                    "in": {
                        "product_info": {
                            "$arrayElemAt": [
                                {
                                    "$filter": {
                                        "input": "$products_info",
                                        "as": "p",
                                        "cond": {
                                            "$eq": ["$$p._id", "$$product.product"]
                                        }
                                    }
                                },
                                0
                            ]
                        },
                        "quantity": "$$product.quantity"
                    }
                }
            },
            "price": 1,
            "type": 1,
            "status": 1
        }
    }
]