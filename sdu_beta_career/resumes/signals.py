from sdu_beta_career.users.models import Profile
from sdu_beta_career.resumes.models import Resume
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=Profile)
def create_resume(sender, instance, created, **kwargs):
    if created:
        Resume.objects.create(profile=instance)


@receiver(post_save, sender=Profile)
def create_resume_save(sender, instance, **kwargs):
    instance.resume.save()
