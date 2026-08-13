from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_contact_notification(contact_id):
    """Email the team when a new contact message arrives (runs in background)."""
    from .models import ContactMessage

    try:
        msg = ContactMessage.objects.get(pk=contact_id)
    except ContactMessage.DoesNotExist:
        return

    send_mail(
        subject=f"New enquiry from {msg.name}",
        message=(
            f"Name: {msg.name}\nEmail: {msg.email}\nPhone: {msg.phone}\n"
            f"Subject: {msg.subject}\n\n{msg.message}"
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
        fail_silently=True,
    )
