# Generated by Django 2.2.28 on 2025-03-31 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delegate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('role', models.CharField(max_length=50)),
                ('function', models.CharField(max_length=50)),
                ('lc', models.CharField(max_length=100)),
                ('lc_password', models.CharField(max_length=100)),
                ('allergies', models.CharField(max_length=10)),
                ('allergy_details', models.TextField(blank=True, null=True)),
                ('tshirt_size', models.CharField(max_length=5)),
                ('tshirt_quantity', models.PositiveIntegerField(default=0)),
                ('id_front', models.FileField(blank=True, null=True, upload_to='uploads/id_front/')),
                ('id_back', models.FileField(blank=True, null=True, upload_to='uploads/id_back/')),
                ('indemnity_form', models.FileField(blank=True, null=True, upload_to='uploads/indemnity_forms/')),
                ('delegate_id', models.CharField(editable=False, max_length=20, unique=True)),
            ],
        ),
    ]
