from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from form.models import UserProfile


def form(request):
    if request.method == 'POST':
        # username = request.POST['username']
        name = request.POST['name']
        dob = request.POST['dob']
        number = request.POST['number']
        gender = request.POST['gender']
        email = request.POST['email']
        street = request.POST['street']
        city = request.POST['city']
        state = request.POST['state']
        postal = request.POST['postal']
        country = request.POST['country']
        district = request.POST['district']
        account = request.POST['account']
        credit_card = request.POST.get('credit_card')
        debit_card = request.POST.get('debit_card')
        cheque_book = request.POST.get('cheque_book')

        user = UserProfile(
            # username=username,
            name=name,
            dob=dob,
            number=number,
            gender=gender,
            email=email,
            street=street,
            city=city,
            state=state,
            postal=postal,
            country=country,
            district=district,
            account=account,
            debit_card=debit_card,
            credit_card=credit_card,
            cheque_book=cheque_book,
        )
        user.save()

        messages.success(request, 'User profile created successfully.')

        return redirect('/')

    return render(request, "form.html")