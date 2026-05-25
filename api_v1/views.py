from rest_framework import viewsets
from .models import Journal
from .serializers import JournalSerializer


class JournalViewSet(viewsets.ModelViewSet):
    serializer_class = JournalSerializer
    queryset = Journal.objects.all()

    def get_queryset(self):
        queryset = Journal.objects.all()

        category = self.request.query_params.get("category")
        publisher = self.request.query_params.get("publisher")

        if category:
            queryset = queryset.filter(category__icontains=category)

        if publisher:
            queryset = queryset.filter(publisher__icontains=publisher)

        return queryset