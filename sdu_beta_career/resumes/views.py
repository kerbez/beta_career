from django.shortcuts import render, get_object_or_404
from sdu_beta_career.resumes.models import Resume
from sdu_beta_career.users.models import Profile


def resume_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    resume_details = Resume(profile=profile)
    return render(request, 'resume.html', {'resume': resume_details})




