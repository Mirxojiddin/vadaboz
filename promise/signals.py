from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from promise.models import Promise, BrokenPromise, PromiseCommit
from promise.send_mail import send_email


@receiver(pre_save, sender=Promise)
def create_broken_promise(sender, instance, **kwargs):
    if instance.pk:
        previous_promise = Promise.objects.get(pk=instance.pk)
        broken_promise = BrokenPromise.objects.filter(promise=previous_promise)
        if previous_promise.status != 'failed' and instance.status == 'failed' and len(broken_promise) == 0:
            BrokenPromise.objects.create(user=instance.user, promise=instance, cause="Status changed to failed")


@receiver(pre_save, sender=Promise)
def create_finished_promise(sender, instance, **kwargs):
    if instance.pk:
        previous_promise = Promise.objects.get(pk=instance.pk)
        finished_promise = BrokenPromise.objects.filter(promise=previous_promise)
        if previous_promise.status != 'finished' and instance.status == 'finished' and len(finished_promise) == 0:
            BrokenPromise.objects.create(user=instance.user, promise=instance, cause="Status changed to failed")


@receiver(post_save, sender=PromiseCommit)
def send_welcome_email(sender, instance, created, **kwargs):
    print('salom')
    if instance.pk:
        subject = f"Add commit your promise"
        message = f"Hi {instance.promise.user.first_name}, {instance.user.get_full_name()} write you a commit to "\
                  f"{instance.promise.title} promise. <br>Comiit {instance.commit}"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_emails = instance.promise.user.email
        send_email(subject, message, from_email, to_emails)
