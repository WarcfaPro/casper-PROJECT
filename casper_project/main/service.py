
def _get_full_company_name(request):
    full_company_name = request.user.company_type + ' ' + request.user.company_name
    return full_company_name
