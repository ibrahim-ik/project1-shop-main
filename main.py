from shop import (
    print_menu,
    print_originals,
    print_signatures,
    get_order,
    print_order,
    get_total_price,

)

print_menu()
print_originals()
print_signatures()
order_list = get_order()
print_order(order_list)