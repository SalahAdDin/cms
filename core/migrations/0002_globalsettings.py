# Generated by Django 2.0.5 on 2018-05-19 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_telephone', models.CharField(max_length=255, verbose_name='Telephone')),
                ('contact_email', models.EmailField(max_length=255, verbose_name='Email address')),
                ('contact_twitter', models.CharField(max_length=255, verbose_name='Twitter')),
                ('contact_facebook', models.CharField(max_length=255, verbose_name='Facebook')),
                ('contact_linked_in', models.CharField(max_length=255, verbose_name='Linked In')),
                ('contact_google_plus', models.CharField(max_length=255, verbose_name='Google Plus')),
                ('contact_youtube', models.CharField(max_length=255, verbose_name='YouTube')),
                ('email_newsletter_teaser', models.CharField(help_text='Text that sits above the email newsletter', max_length=255, verbose_name='News letter teaser')),
                ('email_mailing_list', models.CharField(max_length=255, verbose_name='Mailing list e-mail')),
                ('office_address_title', models.CharField(help_text='Address title', max_length=255, verbose_name='Office address title')),
                ('office_address', models.CharField(help_text='Full address', max_length=255, verbose_name='Office address')),
                ('office_address_link', models.URLField(help_text='Link to google maps', max_length=255, verbose_name='Office address link')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Global Setting',
                'verbose_name_plural': 'Global Settings',
            },
        ),
    ]