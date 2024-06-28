from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from promise.models import Promise, BrokenPromise


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