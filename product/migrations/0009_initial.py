# Generated by Django 4.2 on 2024-04-27 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0008_remove_product_categories_remove_product_sizes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('slug', models.SlugField(max_length=255, verbose_name='слаг')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('description', models.TextField(verbose_name='опесание')),
                ('price', models.PositiveIntegerField(verbose_name='цена')),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_media', to='product.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/product/', verbose_name='фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_media', to='product.product')),
            ],
            options={
                'verbose_name': 'Медиа Продукта',
                'verbose_name_plural': 'Медии Продуктов',
            },
        ),
    ]
