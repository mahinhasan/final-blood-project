# Generated by Django 3.1.6 on 2021-07-03 10:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident', models.CharField(max_length=254)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('O+', 'O+'), ('O-', 'O-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('district', models.CharField(choices=[('Barguna', 'Barguna'), ('Barishal', 'Barishal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chattogram', 'Chattogram'), ('Cumilla', 'Cumilla'), ('Feni', 'Feni'), ('Khagrachhari', 'Khagrachhari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Tangail', 'Tangail'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Chuadanga'), ('Jashore', 'Jashore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira'), ('Jamalpur', 'Jamalpur'), ('Mymensingh', 'Mymensingh'), ('Netrokona', 'Netrokona'), ('Sherpur', 'Sherpur'), ('Bagura', 'Bagura'), ('Joypurhat', 'Joypurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Chapainawabganj', 'Chapainawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajganj', 'Sirajganj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Nilphamari'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Habiganj', 'Habiganj'), ('Moulvibazar', 'Moulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet')], max_length=50)),
                ('division', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Sylhet', 'Sylhet'), ('Barisal', 'Barisal'), ('Khulna', 'Khulna'), ('Chittagong', 'Chittagong'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh'), ('Comilla', 'Comilla'), ('Faridpur', 'Faridpur')], max_length=50)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
