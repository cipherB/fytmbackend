from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Board
from card.models import Card, CheckList
from .serializers import BoardSerializer
from django.http import JsonResponse

# Create your views here.

# register an account
class CreateBoard(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


# get all workspace
class GetBoards(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: 
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

class RetrieveUpdateBoard(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    lookup_fields = ['id',]

def chart_stats(request, id):
    board_cards = list(Card.objects.filter(board=id).values_list('id', flat=True))
    open = list(Card.objects.filter(board=id, status="open").values_list('id', flat=True))
    in_progress = list(Card.objects.filter(board=id, status="in progress").values_list('id', flat=True))
    need_assistance = list(Card.objects.filter(board=id, status="need assistance").values_list('id', flat=True))
    on_hold = list(Card.objects.filter(board=id, status="on hold").values_list('id', flat=True))
    client_review = list(Card.objects.filter(board=id, status="client review").values_list('id', flat=True))
    verify_close = list(Card.objects.filter(board=id, status="verify and close").values_list('id', flat=True))
    done= list(Card.objects.filter(board=id, status="done").values_list('id', flat=True))
    urgent = list(Card.objects.filter(board=id, priority="urgent").values_list('id', flat=True))
    high = list(Card.objects.filter(board=id, priority="high").values_list('id', flat=True))
    normal = list(Card.objects.filter(board=id, priority="normal").values_list('id', flat=True))
    low = list(Card.objects.filter(board=id, priority="low").values_list('id', flat=True))
    no_priority = list(Card.objects.filter(board=id, priority="no priority").values_list('id', flat=True))
    checklist_stat = list((CheckList.objects.filter(card__in=[checklist for checklist in board_cards]).values_list('id', flat=True)))
    checked_stat = list((CheckList.objects.filter(card__in=[checklist for checklist in board_cards], status=True).values_list('id', flat=True)))
    unchecked_stat = list((CheckList.objects.filter(card__in=[checklist for checklist in board_cards], status=False).values_list('id', flat=True)))
    return JsonResponse({
        'checklists_total': len(checklist_stat), 
        'checked': len(checked_stat), 
        'unchecked': len(unchecked_stat), 
        'open': len(open),
        'in_progress': len(in_progress),
        'need_assistance': len(need_assistance),
        'on_hold': len(on_hold),
        'client_review': len(client_review),
        'verify_close': len(verify_close),
        'done': len(done),
        'urgent': len(urgent),
        'high': len(high),
        'normal': len(normal),
        'low': len(low),
        'no_priority': len(no_priority)
        })
