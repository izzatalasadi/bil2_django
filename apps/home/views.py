
import csv

from django import template
from django.core.mail import BadHeaderError, send_mail
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse

from .models import Caritems


def load_cars():
    """
    Save car data from cars.csv file to the database
    """

    with open("cars.csv", 'r') as f:
        reader = csv.reader(f)
        data = list(reader)[1:]
        Caritems.objects.all().delete()
        for row in data:
            try:
                price = int(str(row[4]).strip().replace(",", ""))
            except ValueError:
                # Skip rows where price is not a valid integer
                continue

            car = {
                'image': row[0],
                'km': row[1],
                'model': row[2],
                'model_type': row[3],
                'price': price,
                'url': row[5],
                'year': row[6],
            }
            Caritems(**car).save()


def buyView(request):
    """
    Filter Caritems based on search parameters and paginate the results
    """
    if request.method == 'POST':
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        car = request.POST.get('car')
        message = request.POST.get('message')

        try:
            send_mail(name, mobile, car, message, ["izzat.alasadi@gmail.com"])
            return HttpResponseRedirect("/success/")

        except BadHeaderError:
            return render(request, "home/404.html")
    else:
        empty_list = []
        cars = Caritems.objects.all()

        selected_models = request.GET.getlist('model')
        if request.GET.get('min_price'):
            cars = cars.filter(price__gte=request.GET.get('min_price'))

        if request.GET.get('max_price'):
            cars = cars.filter(price__lte=request.GET.get('max_price'))

        if request.GET.get('min_year'):
            cars = cars.filter(year__gte=request.GET.get('min_year'))

        if request.GET.get('max_year'):
            cars = cars.filter(year__lte=request.GET.get('max_year'))

        if selected_models:
            cars = cars.filter(model__in=selected_models)

        # Perform the query to get the count of each model
        models = cars.values('model').distinct()

        # Order the queryset by the created_at field
        cars = cars.order_by('id').distinct()

        # Paginate the results
        paginator = Paginator(cars, 18)  # 18 items per page
        page = request.GET.get('page')
        cars = paginator.get_page(page)

        return render(request, "home/buy.html", {'cars': cars, 'selected_models': selected_models, 'models': models, 'empty_list': empty_list})


def index(request):
    return render(request, "home/index.html")


def pages(request):
    context = {}

    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/404.html')
        return HttpResponse(html_template.render(context, request))


def aboutView(request):
    return render(request, "home/about.html")


def serviceView(request):
    return render(request, "home/service.html")


def contactView(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('phone')
        message = request.POST.get('message')
        try:
            send_mail(name, email, subject, message,
                      ["izzat.alasadi@gmail.com"])
            return HttpResponseRedirect("/success/")
        except BadHeaderError:
            return HttpResponse("Invalid header found.")
    else:
        return render(request, "home/contact.html")


def successView(request):
    return render(request, "home/success.html")


def sellView(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        files = request.POST.get('myFile')
        message = request.POST.get('message')

        try:
            send_mail(name, message, mobile, files,
                      ["izzat.alasadi@gmail.com"])
            return HttpResponseRedirect("/success/")

        except BadHeaderError:
            return render(request, "home/404.html")
    else:
        return render(request, "home/sell.html")


def bookView(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        car = request.POST.get('car')
        message = request.POST.get('message')

        try:
            send_mail(name, mobile, car, message, ["izzat.alasadi@gmail.com"])
            return HttpResponseRedirect("/success/")

        except BadHeaderError:
            return render(request, "home/404.html")
