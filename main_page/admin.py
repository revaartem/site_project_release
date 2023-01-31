from django.contrib import admin
from .models import Category, Dishes, Events, Gallery, Photo, TableReservation, AboutUs, HomeSliderInfo,\
    BlockOfInformation, InformationInBlocks, CrewBlock, CrewMember, CustomerFeedback
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_description', 'event_date_and_time', 'position', 'is_visible']
    list_editable = ['event_date_and_time', 'position', 'is_visible']

@admin.register(Dishes)
class DishesAdmin(admin.ModelAdmin):
    list_filter = ('category', 'position', )
    list_display = ['name', 'position', 'is_visible', 'price', 'photo', 'category']
    list_editable = ['position', 'is_visible', 'price']
    prepopulated_fields = {'slug': ('name', ), }


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_filter = ('position', )
    list_display = ['title', 'position', 'is_visible']
    list_editable = ['position', 'is_visible']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_filter = ('position', 'gallery')
    list_display = ['title', 'position', 'gallery', 'photo', 'is_visible']
    list_editable = ['position', 'gallery', 'is_visible']


@admin.register(TableReservation)
class TableReservationAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'name_of_customer', 'email', 'phone_number', 'number_of_people', 'additional_message']
    list_editable = ['number_of_people', 'additional_message']
    list_filter = ('date', )


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['header', 'heading_text', 'font_photo']
    list_editable = ['heading_text']


@admin.register(HomeSliderInfo)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['header', 'heading_text', 'video']
    list_editable = ['heading_text']


class BlockOfInformationAdmin(admin.TabularInline):
    model = BlockOfInformation
    raw_id_fields = ['block']


@admin.register(InformationInBlocks)
class InformationInBlocksAdmin(admin.ModelAdmin):
    list_display = ['header', 'heading_text']
    inlines = [BlockOfInformationAdmin]


class CrewMemberAdmin(admin.TabularInline):
    model = CrewMember
    raw_id_fields = ['crew']


@admin.register(CrewBlock)
class CrewBlockAdmin(admin.ModelAdmin):
    list_display = ['header', 'heading_text']
    inlines = [CrewMemberAdmin]


@admin.register(CustomerFeedback)
class CustomerFeedbackAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'comment', 'is_visible', 'customer_photo']
    list_editable = ['comment', 'is_visible']
