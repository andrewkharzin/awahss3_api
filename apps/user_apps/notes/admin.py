from django.contrib import admin
from .models import FileAttachment, ImageAttachment, Note, Category, Tag
from mptt.admin import DraggableMPTTAdmin

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Tag, TagAdmin)

class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'icon')
    list_display_links = ('indented_title',)
    list_filter = ('parent',)
    search_fields = ('name',)

    def get_ordering(self, request):
        return ['tree_id', 'lft']

class FileAttachmentInline(admin.TabularInline):
    model = FileAttachment


class ImageAttachmentInline(admin.StackedInline):
    model = ImageAttachment


@admin.register(FileAttachment)
class FileAttachmentAdmin(admin.ModelAdmin):
    pass


@admin.register(ImageAttachment)
class ImageAttachmentAdmin(admin.ModelAdmin):
    pass


class NoteAdmin(admin.ModelAdmin):
    inlines = [FileAttachmentInline, ImageAttachmentInline]
    list_display = ('title', 'author', 'category', 'tags_display')

    def tags_display(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    tags_display.short_description = 'Tags'


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
