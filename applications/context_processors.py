from applications.home.models import Home


def home_contact(request):
    home = Home.objects.latest('created')
    return {'phone': home.phone, 'contact_email': home.contact_email} if (home.phone or home.contact_email) else {}
