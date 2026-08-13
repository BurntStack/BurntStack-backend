"""Populate the database with initial demo content for the website.

Usage:  python manage.py seed
"""

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.blog.models import Category, Post
from apps.careers.models import JobOpening
from apps.faqs.models import Faq
from apps.projects.models import Project
from apps.testimonials.models import Testimonial


class Command(BaseCommand):
    help = "Seed the database with demo content (idempotent)."

    def handle(self, *args, **options):
        self._seed_projects()
        self._seed_testimonials()
        self._seed_faqs()
        self._seed_jobs()
        self._seed_blog()
        self.stdout.write(self.style.SUCCESS("Database seeded successfully."))

    def _seed_projects(self):
        data = [
            {
                "name": "MediSync Health Platform", "category": "Healthcare",
                "tech": ["React", "Django", "PostgreSQL", "AWS"],
                "problem": "A hospital network needed to unify patient records across five legacy systems.",
                "solution": "A HIPAA-aligned platform with real-time sync, RBAC and analytics.",
                "results": "40% faster onboarding and a single source of truth across 12 facilities.",
                "is_featured": True, "order": 1,
            },
            {
                "name": "FinTrack Analytics", "category": "Finance",
                "tech": ["React", "Python", "Redis", "TensorFlow"],
                "problem": "A fintech wanted AI insights without a data-science team.",
                "solution": "A predictive analytics dashboard with anomaly detection.",
                "results": "Detected fraud 3x earlier and cut reporting time by 80%.",
                "is_featured": True, "order": 2,
            },
            {
                "name": "ShopWave Commerce", "category": "E-Commerce",
                "tech": ["React", "Django REST", "PostgreSQL", "Docker"],
                "problem": "A retail brand was losing sales to a slow, dated storefront.",
                "solution": "A headless commerce rebuild with one-page checkout and search.",
                "results": "2.4x conversion uplift and 55% fewer abandoned carts.",
                "is_featured": True, "order": 3,
            },
        ]
        for item in data:
            Project.objects.update_or_create(name=item["name"], defaults=item)

    def _seed_testimonials(self):
        data = [
            {"name": "Ananya Rao", "company": "CEO, MediSync", "rating": 5, "order": 1,
             "review": "BurntStack rebuilt our entire platform in record time. World-class quality and communication."},
            {"name": "Daniel Fischer", "company": "CTO, FinTrack", "rating": 5, "order": 2,
             "review": "Their AI expertise is the real deal. The analytics engine pays for itself every month."},
            {"name": "Priya Menon", "company": "Founder, ShopWave", "rating": 5, "order": 3,
             "review": "Conversions more than doubled after the rebuild. Thoughtful engineering at every step."},
        ]
        for item in data:
            Testimonial.objects.update_or_create(
                name=item["name"], company=item["company"], defaults=item
            )

    def _seed_faqs(self):
        data = [
            ("How long does development take?", "Most websites ship in 3–6 weeks and enterprise platforms in 3–6 months.", 1),
            ("Do you provide support?", "Yes — every engagement includes a support window, with optional ongoing maintenance and SLAs.", 2),
            ("Can you redesign existing websites?", "Absolutely. We frequently modernise legacy sites and platforms.", 3),
            ("Which technologies do you use?", "React, Python/Django, PostgreSQL, AWS and modern AI tooling — chosen per project.", 4),
            ("Do you sign NDAs?", "Yes, we're happy to sign an NDA before discussing your project in detail.", 5),
            ("How does payment work?", "We work in milestone-based payments tied to deliverables, with flexible retainer terms.", 6),
        ]
        for question, answer, order in data:
            Faq.objects.update_or_create(
                question=question, defaults={"answer": answer, "order": order}
            )

    def _seed_jobs(self):
        data = [
            {"title": "Senior Frontend Engineer", "department": "Engineering", "location": "Hyderabad / Remote",
             "description": "Build beautiful, performant React interfaces for ambitious products."},
            {"title": "Backend Engineer (Django)", "department": "Engineering", "location": "Hyderabad / Remote",
             "description": "Design and scale secure REST APIs with Python, Django and PostgreSQL."},
            {"title": "Machine Learning Engineer", "department": "AI", "location": "Remote",
             "description": "Ship LLM copilots and predictive models from prototype to production."},
        ]
        for item in data:
            JobOpening.objects.update_or_create(title=item["title"], defaults=item)

    def _seed_blog(self):
        eng, _ = Category.objects.get_or_create(name="Engineering")
        ai, _ = Category.objects.get_or_create(name="AI")
        posts = [
            {"title": "Scaling Django to Millions of Requests", "category": eng, "is_featured": True,
             "excerpt": "Battle-tested caching, indexing and async-worker patterns that keep Django fast under load.",
             "tags": ["Django", "Performance", "Scaling"], "reading_time": 8},
            {"title": "Building LLM Copilots Your Team Will Actually Use", "category": ai, "is_featured": False,
             "excerpt": "A practical guide to shipping AI assistants that are helpful, safe and grounded in your data.",
             "tags": ["AI", "LLM", "Product"], "reading_time": 6},
        ]
        for item in posts:
            Post.objects.update_or_create(
                title=item["title"],
                defaults={
                    **item,
                    "content": "Full article content goes here.",
                    "is_published": True,
                    "published_at": timezone.now(),
                },
            )
