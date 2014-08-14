from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response

from quotations.serializers import UserSerializer, GroupSerializer
from quotations.models import Author, Quote, Subject
from quotations.serializers import AuthorSerializer, QuoteSerializer, SubjectSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows authors to be viewed or edited.
    """    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quotes to be viewed or edited.
    """    
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get_queryset(self):   
        if self.request.GET.get('author'):     
            author = self.request.GET.get('author', '1')
            author_qs = Author.objects.get(pk=author)

            subject = self.request.GET.get('subject', '1')
            subject_qs = Subject.objects.get(pk=subject)

            # quote_qs = Quote.objects.filter(author=author_qs)
            return subject_qs.quotes.filter(author=author_qs)
        else:
            return Quote.objects.all()

class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows subjects to be viewed or edited.
    """   
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create(self, request):
        if self.request.DATA.get('text'):
            author = self.request.DATA.get('author', '1')
            author_qs = Author.objects.get(pk=author)

            quote = self.request.DATA.get('text', '')
            quote_qs = Quote.objects.create(text=quote, author=author_qs)

            subject = self.request.DATA.get('name', '1')
            subject_qs = Subject.objects.get(pk=subject)

            subject_qs.quotes.add(quote_qs)
            return Response({"message":"quote added to subject"})
        else:
            Subject.objects.create(name=request.DATA.get('name')) #not getting name
            return Response({"message":"subject created"})

