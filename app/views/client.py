from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import View

from app.filters import LetterFilter
from app.forms import CreateLetterForm
from app.models import Letter, Staff


def client_letter(request):
    letters_queryset = Letter.objects.all()
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

    context = {
        'letters': letters_queryset,
        'my_filter': my_filter
    }
    return render(request, 'app/client/letter.html', context)


def client_new_letter(request):
    staff_queryset = Staff.objects.all()
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


def client_report(request):
    reports = Staff.objects.all()
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


def create_letter(request):
    if request.method == 'POST':
        form = CreateLetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            # letter.client_id = request.user
            letter.client_id = 1
            letter.save()
            return render(request, 'app/client/create-letter.html', {'form': form})
    else:
        form = CreateLetterForm()
    return render(request, 'app/client/create-letter.html', {'form': form})
