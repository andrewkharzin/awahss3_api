from rest_framework import viewsets
from apps.user_apps.notes.models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



@api_view(['GET'])
def note_categories(request):
    """
    Retrieve a list of categories associated with notes.
    """
    # Get all unique categories associated with at least one note
    categories = Category.objects.filter(note__isnull=False).distinct()

    # Serialize the categories to get their names
    category_names = [category.name for category in categories]

    return Response(category_names)