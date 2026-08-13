"""Create access-control roles (Groups) for the Django admin.

Superusers always have full access. This command defines scoped staff roles so
you can grant limited admin access instead of handing out superuser rights.

Usage:  python manage.py setup_roles

Then, in the admin (Users), mark a user as "Staff", add them to one or more of
the groups below, and they'll only see/act on the models their role allows.
"""

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

# Role -> {"app.model": [actions]}   actions ⊆ {add, change, delete, view}
ROLES = {
    "Content Editors": {
        "blog.category": ["add", "change", "delete", "view"],
        "blog.post": ["add", "change", "delete", "view"],
        "projects.project": ["add", "change", "delete", "view"],
        "testimonials.testimonial": ["add", "change", "delete", "view"],
        "faqs.faq": ["add", "change", "delete", "view"],
    },
    "Recruiters": {
        "careers.jobopening": ["add", "change", "delete", "view"],
        # Applications are read/triage only — no creating or deleting candidates.
        "careers.application": ["change", "view"],
    },
    "Support": {
        # Inbound messages are triage only (mark handled); never create/delete.
        "contact.contactmessage": ["change", "view"],
        "newsletter.subscriber": ["change", "view"],
    },
}


class Command(BaseCommand):
    help = "Create/refresh admin access-control roles (Groups with scoped permissions)."

    def handle(self, *args, **options):
        for role_name, model_perms in ROLES.items():
            group, created = Group.objects.get_or_create(name=role_name)
            perms = []
            for dotted, actions in model_perms.items():
                app_label, model = dotted.split(".")
                try:
                    ct = ContentType.objects.get(app_label=app_label, model=model)
                except ContentType.DoesNotExist:
                    self.stderr.write(
                        self.style.WARNING(f"  skip {dotted} (run migrate first)")
                    )
                    continue
                for action in actions:
                    codename = f"{action}_{model}"
                    try:
                        perms.append(Permission.objects.get(content_type=ct, codename=codename))
                    except Permission.DoesNotExist:
                        self.stderr.write(self.style.WARNING(f"  missing perm {codename}"))

            # set() makes this idempotent: re-running syncs the role to this spec.
            group.permissions.set(perms)
            status = "created" if created else "updated"
            self.stdout.write(
                self.style.SUCCESS(f"{status}: {role_name} ({len(perms)} permissions)")
            )

        self.stdout.write(
            self.style.SUCCESS(
                "\nRoles ready. Assign staff users to these groups in the admin -> Users."
            )
        )
