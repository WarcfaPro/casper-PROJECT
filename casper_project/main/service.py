def _get_full_company_name(request):
    full_company_name = request.user.company_type + ' ' + request.user.company_name
    return full_company_name


def _get_full_address(city, street):
    full_address = city + ', ' + street
    return full_address


def _order_form_save(request, order_form):
    orders = order_form.save(commit=False)
    orders.company_id = request.user.pk
    orders.company_name = request.user.company_name
    orders.full_address = _get_full_address(orders.address_city, orders.address_street)
    orders.full_address_to = _get_full_address(orders.address_city_to, orders.address_street_to)
    orders.save()


def _order_carrier_form_save(request, form):
    order = form.save(commit=False)
    order.order = request.order
    order.carrier = request.user
    order.save()
