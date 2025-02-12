from django.http import HttpResponse
from django.template import loader
from .models import Member
import datetime
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import ContactBook
from .serializers import ContactSerializer

# Create your views here.


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    today = datetime.datetime.today().weekday()
    greeting = 0 if today == 6 else 1
    mymembers = Member.objects.all().values()
    mydata = Member.objects.all()
    mydata_1 = Member.objects.values_list('firstname')
    mydata_2 = Member.objects.filter(firstname='<name>').values()
    # In SQL, the above _-^-_ statement would be written like this:
    # SELECT * FROM members WHERE firstname = '<name>';
    mydata_3 = Member.objects.filter(lastname='<name>', id=3).values()
    # In SQL, the above _-^-_ statement would be written like this:
    # SELECT * FROM members WHERE lastname = '<name>' AND id = 3;
    mydata_4 = Member.objects.filter(firstname='<name>').values() | Member.objects.filter(firstname='<name>').values()
    mydata_5 = Member.objects.filter(Q(firstname='<name>') | Q(firstname='<name>')).values()
    # In SQL, the above _-^-_ statement would be written like this:
    # SELECT * FROM members WHERE firstname = '<name>' OR firstname = '<name>';
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Usman',
        'greeting': greeting,
        'fruits': ['Apple', 'Banana', 'Cherry', 'Orange', 'Kiwi'],
        'mymembers': mymembers,
        'members': mydata,
        'members_1': mydata_1,
        'members_2': mydata_2,
        'members_3': mydata_3,
        'members_4': mydata_4,
        'members_5': mydata_5,
        'cars': [
            {
                'brand': 'Ford',
                'model': 'Mustang',
                'year': '1964',
            },
            {
                'brand': 'Ford',
                'model': 'Bronco',
                'year': '1970',
            },
            {
                'brand': 'Volvo',
                'model': 'P1800',
                'year': '1964',
            },
        ],
        'emptysetobject': [],
    }
    return HttpResponse(template.render(context, request))


# # Creating a contact book:-

# # Contact book dictionary to store contacts:
# contact_book = {
#     'Ambulance': '115',
#     'Firefighting': '16',
#     'Police': '15',
#     'Punjab Women Helpline': '1043',
#     'Provincial Disaster Management Authority (PDMA)': '1129',
#     'Rescue 1122': '042-99231701-2',
# }

# # Function to add a new contact:
# def add_contact(name, phone):
#     if name in contact_book:
#         print(f"Contact for {name} already exists.")
#     else:
#         contact_book[name] = phone
#         print(f"Contact for {name} added.")


# # Function to view all contacts:
# def view_contacts():
#     if contact_book:
#         print("Contact Book:")
#         for name, phone in contact_book.items():
#             print(f"{name}: {phone}")
#     else:
#         print("No contacts available.")
# # .......


class ContactBookViewSet(viewsets.ModelViewSet):
    queryset = ContactBook.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            contact_name = response.data.get('firstname', 'lastname')
            print(f"A new contact '{contact_name}' has been added successfully!")

        return response
