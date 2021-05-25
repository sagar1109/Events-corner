from django.shortcuts import render
from .models import event
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context={
        'programes': event.objects.all()
    }
    return render(request,'events/home.html',context)
class EventListView(ListView):
    model = event
    template_name='events/home.html'
    context_object_name='programes'
    ordering=['-time']

class EventDetailView(DetailView):
    model = event


class EventCreateView(LoginRequiredMixin,CreateView):
    model = event
    fields=['program','about','venue','time']

    def form_valid(self,form):
        form.instance.head= self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = event
    fields=['program','about','venue','time']

    def form_valid(self,form):
        form.instance.head= self.request.user
        return super().form_valid(form) 

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.head:
            return True
        return False
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.head:
            return True
        return False
