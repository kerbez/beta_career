from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Company
from sdu_beta_career.vacancies.models import Vacancy
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
import operator


def company_list(request):
    companies = Company.objects.filter()
    return render(request, 'company_list.html', {'companies': companies})


def company_detail(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'company_detail.html', {'company': company})


def company_search(request):
    companies = Company.objects.filter()
    return render(request, 'company_search.html', {'companies': companies})


def get_queryset(request):
    result = Company.objects.all()
    query = request.GET.get('q')
    query_by_option = request.GET.get('by_option')

    if query_by_option:
        if query_by_option == "searchVacancy":
            if query:
                result = Vacancy.objects.filter(Q(name__icontains=query) |
                                                Q(responsibility__icontains=query) | Q(requirements__icontains=query) |
                                                Q(conditions__icontains=query) | Q(skills__icontains=query) |
                                                Q(busyness__icontains=query))
                return render(request, 'vacancy_search.html', {'vacancies': result})
        else:
            if query:
                result = Company.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'company_search.html', {'companies': result})


class CompaniesSearchView(ListView):
    context_object_name = 'companies'
    queryset = Company.objects.all()
    template_name = 'company_search.html'


