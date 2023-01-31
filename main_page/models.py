from django.db import models
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

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
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
    event_description = models.CharField(max_length=500)
    event_date_and_time = models.DateTimeField(help_text='Enter date and time of event')
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name, blank=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class Gallery(models.Model):
    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class Photo(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('photo/', new_filename)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', 'gallery', )


class TableReservation(models.Model):

    date = models.DateField(help_text='Date of reservation.')
    time = models.TimeField(help_text='Time of reservation.')
    name_of_customer = models.CharField(max_length=50)
    email = models.CharField(max_length=65)
    phone_number = models.CharField(max_length=20)
    number_of_people = models.SmallIntegerField()
    additional_message = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return f'{self.date},|{self.time}|'


class AboutUs(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('about_us/', new_filename)

    header = models.CharField(max_length=80, help_text='Header text.')
    heading_text = models.TextField(max_length=255, help_text='Heading text')
    font_photo = models.ImageField(upload_to=get_file_name)


class HomeSliderInfo(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('home_slider/', new_filename)

    header = models.CharField(max_length=80, help_text='Header text.')
    heading_text = models.TextField(max_length=255, help_text='Heading text')
    video = models.URLField(blank=True, help_text='Paste here URL to the video.',)


class InformationInBlocks(models.Model):

    header = models.CharField(max_length=80)
    heading_text = models.TextField(max_length=255)

    def __str__(self):
        return f'Block with header "{self.header}"'


class BlockOfInformation(models.Model):

    block_number = models.SmallIntegerField()
    block_title = models.CharField(max_length=50)
    block_text = models.TextField(max_length=255)
    block = models.ForeignKey(InformationInBlocks, on_delete=models.CASCADE)

    def __str__(self):
        return f'Block {self.block_number}'


class CrewBlock(models.Model):

    header = models.CharField(max_length=80)
    heading_text = models.TextField(max_length=255)

    def __str__(self):
        return f'Crew block with header "{self.header}"'


class CrewMember(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_of_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_of_file}'
        return os.path.join('member_photos/', new_filename)

    member_name = models.CharField(max_length=50)
    member_description = models.TextField(max_length=255)
    crew = models.ForeignKey(CrewBlock, on_delete=models.CASCADE)
    member_photo = models.ImageField(upload_to=get_file_name)
    twitter_link = models.URLField(help_text='Input here URL to Twitter account.')
    facebook_link = models.URLField(help_text='Input here URL to Facebook account.')
    instagram_link = models.URLField(help_text='Input here URL to Instagram account.')
    linkedin_link = models.URLField(help_text='Input here URL to LinkedIn account.')

    def __str__(self):
        return f'{self.member_name}'


class CustomerFeedback(models.Model):

    customer_name = models.CharField(max_length=50)
    comment = models.TextField(max_length=200)
    is_visible = models.BooleanField(default=True)
    customer_photo = models.ImageField()