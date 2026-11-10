orders = {
    "001": {"owner": "alice", "order_desc": "gold", "amount": 1000},
    "002": {"owner": "bob", "order_desc": "silver", "amount": 2000},
}


# bola, vulnerable
def get_order_vulnerable(current_user, order_id):
    order = orders.get(order_id)
    if order is None:
        return {"status_code": 404, "body": {"error": "Not found"}}
    return {"status_code": 200, "body": order}


# secure version
def get_order_secure(current_user, order_id):
    order = orders.get(order_id)
    if order is None:
        return {"status_code": 404, "body": {"error": "Not found"}}
    if order["owner"] != current_user:
        return {"status_code": 404, "body": {"error": "Not found"}}
    return {"status_code": 200, "body": order}
