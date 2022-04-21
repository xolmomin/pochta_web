from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.decorators import permission_classes

from app.filters import LetterFilter
from app.forms import CreateLetterForm
from app.models import Letter, Staff, Region, District
from app.permissions import IsClientMixin
from app.utils.generate_barcode import generate_number


@permission_classes((IsClientMixin,))
def client_letter(request):
    letters_queryset = Letter.objects.order_by('-id')
    page = request.GET.get('page', 1)

    my_filter = LetterFilter(request.GET, letters_queryset)
    letters_queryset = my_filter.qs

    paginator = Paginator(letters_queryset, 10)
    try:
        letters_queryset = paginator.page(page)
    except PageNotAnInteger:
        letters_queryset = paginator.page(1)
    except EmptyPage:
        letters_queryset = paginator.page(paginator.num_pages)
    region = Region.objects.all()
    districts = District.objects.all()
    context = {
        'letters': letters_queryset,
        'my_filter': my_filter,
        "regions": region,
        "districts": districts
    }
    return render(request, 'app/client/letter.html', context)


@permission_classes((IsClientMixin,))
def client_new_letter(request):
    staff_queryset = Staff.objects.order_by('-id')
    page = request.GET.get('page', 1)

    # my_filter = LetterFilter(request.GET, staff_queryest)
    # staff_queryest = my_filter.qs

    paginator = Paginator(staff_queryset, 10)
    try:
        staff_queryset = paginator.page(page)
    except PageNotAnInteger:
        staff_queryset = paginator.page(1)
    except EmptyPage:
        staff_queryset = paginator.page(paginator.num_pages)

    context = {
        'clients': staff_queryset,
        # 'my_filter': my_filter
    }
    return render(request, 'app/client/new-letter.html', context)


@permission_classes((IsClientMixin,))
def client_report(request):
    reports = Staff.objects.order_by('-id')
    page = request.GET.get('page', 1)

    # my_filter = LetterFilter(request.GET, staff_queryest)
    # staff_queryest = my_filter.qs

    paginator = Paginator(reports, 10)
    try:
        reports = paginator.page(page)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)

    context = {
        'reports': reports,
        # 'my_filter': my_filter
    }
    return render(request, 'app/client/report.html', context)


@permission_classes((IsClientMixin,))
def create_letter(request):
    if request.method == 'POST':
        form = CreateLetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.client = request.user
            if request.user.region:
                code = request.user.region.code
                while 1:
                    barcode = generate_number([int(i) for i in str(code)])
                    if not Letter.objects.filter(barcode=barcode).exists():
                        break
                letter.barcode = barcode
            letter.save()
            return redirect('client_letter_page')
    else:
        form = CreateLetterForm()
    return render(request, 'app/client/create-letter.html', {'form': form})


@permission_classes((IsClientMixin,))
def client_export(request):
    return render(request, 'app/client/export.html')
