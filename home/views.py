from django.shortcuts import render


def index(request):
    """ View to return the index page """

    return render(request, 'home/index.html')


def faq(request):
    """ View the FAQ page """

    return render(request, 'home/faq.html')


def terms_conditions(request):
    """ View the terms and conditions page """

    return render(request, 'home/terms_conditions.html')


def returns(request):
    """ View the returns policy page """

    return render(request, 'home/returns.html')

