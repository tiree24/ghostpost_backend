from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from api.models import BoastRoast
from api.serializers import BoastRoastSerializer
from rest_framework.decorators import action

# Create your views here.
class BoastRoastViewset(viewsets.ModelViewSet):
    queryset = BoastRoast.objects.all().order_by("-date_created")
    serializer_class = BoastRoastSerializer

@action(detail=False)
def Boasts(self, request):
        boast_posts = BoastRoast.objects.filter(post_type=True)
        serializer = self.get_serializer(boast_posts, many=True)
        return Response(serializer.data)

@action(detail=False)
def Roasts(self, request):
        roast_posts = BoastRoast.objects.filter(post_type=False)
        serializer = self.get_serializer(roast_posts, many=True)
        return Response(serializer.data)

@action(detail=False)
def TotalAll(self, request):
        posts = BoastRoast.objects.all().order_by('-total_votes')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

@action(detail=True, methods=['get', 'post'])
def DownVote(self, request, pk=None):
        vote = self.get_object()
        vote.total_votes -= 1
        vote.save()
        return Response(vote.total_votes)

@action(detail=True, methods=['get', 'post'])
def UpVote(self, request, pk=None):
        vote = self.get_object()
        vote.total_votes += 1
        vote.save()
        return Response(vote.total_votes)