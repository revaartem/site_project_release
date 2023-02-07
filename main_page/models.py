from django.core.validators import RegexValidator
from django.db import models
from tinymce.models import HTMLField
import uuid
import os


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )


class Dishes(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('dishes/', new_filename)

    name = models.CharField(unique=True, max_length=50, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    position = models.SmallIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=300, blank=True)
    ingredients = models.CharField(max_length=300)
    is_visible = models.BooleanField(default=True)
    special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', 'price', )
        index_together = (('id', 'slug'), )


class Events(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('events/', new_filename)

    title = models.CharField(unique=True, max_length=70, db_index=True)
    event_description = models.TextField(max_length=500)
    event_date_and_time = models.DateTimeField(help_text='Enter date and time of event')
    event_price = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('event_date_and_time', )


class PhotoToGallery(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('photo/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.photo}'

    class Meta:
        ordering = ('is_visible', )


class AboutUs(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('about_us/', new_filename)

    header = models.CharField(max_length=80, help_text='Header text.')
    heading_text = models.TextField(max_length=700, help_text='Heading text')
    font_photo = models.ImageField(upload_to=get_file_name)
    video_url = models.URLField(help_text='Enter here link to the video.')


class BlockOfInformation(models.Model):

    block_number = models.SmallIntegerField()
    block_title = models.TextField(max_length=50)
    block_text = models.TextField(max_length=255)

    def __str__(self):
        return f'Block {self.block_number}'


class CrewMember(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('member_photos/', new_filename)

    member_name = models.CharField(max_length=50)
    member_description = models.CharField(max_length=80)
    member_photo = models.ImageField(upload_to=get_file_name)
    twitter_link = models.URLField(help_text='Input here URL to Twitter account.')
    facebook_link = models.URLField(help_text='Input here URL to Facebook account.')
    instagram_link = models.URLField(help_text='Input here URL to Instagram account.')
    linkedin_link = models.URLField(help_text='Input here URL to LinkedIn account.')

    def __str__(self):
        return f'{self.member_name}'


class CustomerFeedback(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('customer_feedback/', new_filename)

    customer_name = models.CharField(max_length=50)
    position = models.CharField(max_length=200)
    comment = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)
    customer_photo = models.ImageField()


class HeroSection(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('hero/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class UserReservation(models.Model):

    mobile_re = RegexValidator(regex=r'^(\d{3}[- .]?){2}\d{4}$', message='Phone in format xxx xxx xxxx')
    email_re = RegexValidator(regex=r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\.)+[a-z0-9]{1}'
                                    r'([a-z0-9-]*[a-z0-9])?$', message='Standard e-mail form')

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=63, validators=[email_re])
    phone = models.CharField(max_length=15, validators=[mobile_re])
    date_reservation = models.CharField(max_length=10)
    time_reservation = models.CharField(max_length=10)
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=250, blank=True)
    date_of_the_request = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_of_the_request', )

    def __str__(self):
        return f'{self.name}, {self.phone}: {self.message}'


class ThisIsForTest(models.Model):

    this_is_text = HTMLField(max_length=250)
    this_is_text_2 = HTMLField(max_length=250)
    this_is_text_3 = HTMLField(max_length=250)


class ContactUs(models.Model):

    email_re = RegexValidator(regex=r'^[a-zA-Z0-9]{1}[a-zA-Z0-9_]+(-{1})?[a-zA-Z0-9_]+@{1}([a-zA-Z0-9]+\.)+[a-z0-9]{1}'
                                    r'([a-z0-9-]*[a-z0-9])?$', message='Standard e-mail form')

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=63, validators=[email_re])
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=250, blank=True)
    date_of_the_request = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_of_the_request', )

    def __str__(self):
        return f'{self.name}, {self.email} - {self.subject}'


class InformationInContactUs(models.Model):

    header = models.CharField(max_length=50)
    heading_text = HTMLField(max_length=250)
    location = HTMLField()
    open_hours = HTMLField()
    email = HTMLField()
    call = HTMLField()
    phone_for_top_bar = models.CharField(max_length=15)
    open_hours_for_top_bar = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.header}'


class Footer(models.Model):

    header = HTMLField()
    heading_text = HTMLField(blank=True)
    twitter = models.CharField(max_length=500, blank=True)
    facebook = models.CharField(max_length=500, blank=True)
    instagram = models.CharField(max_length=500, blank=True)
    skype = models.CharField(max_length=500, blank=True)
    linked_in = models.CharField(max_length=500, blank=True)
    site_owner = HTMLField()

    def __str__(self):
        return f'{self.header} - {self.site_owner}'


