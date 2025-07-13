from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from products.models import Product
from reviews.models import Review

User = get_user_model()

class Command(BaseCommand):
    help = 'Load sample data'

    def handle(self, *args, **options):
        # Create admin user
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'role': 'admin',
                'is_staff': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()

        # Create regular user
        regular_user, created = User.objects.get_or_create(
            username='user1',
            defaults={
                'email': 'user1@example.com',
                'role': 'regular'
            }
        )
        if created:
            regular_user.set_password('user123')
            regular_user.save()

        # Create sample products
        products_data = [
            {
                'name': 'Laptop',
                'description': 'High-performance laptop for professionals',
                'price': 999.99
            },
            {
                'name': 'Smartphone',
                'description': 'Latest smartphone with amazing features',
                'price': 699.99
            }
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    **product_data,
                    'created_by': admin_user
                }
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data')
        )