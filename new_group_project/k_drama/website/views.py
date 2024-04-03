from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .models import Show, User
from .forms import ShowForm, UserForm
from rest_framework import generics
from .serializers import ShowSerializer, UserSerializer

# Create your views here.
class Home(View):
    def get(self,request):

        return render(request=request,
                      template_name='website/home.html',
                      context={})
    

class ShowList(View):

    def get(self,request):

        shows = Show.objects.all()

        return render(request = request,
                      template_name = 'website/show_list.html',
                      context = {'shows':shows})
    
class ShowEdit(View):

    def get(self,request,show_id):

        show = Show.objects.get(pk=show_id)
        form = ShowForm(instance=show)

        return render(request = request,
                      template_name = 'website/show_edit.html',
                      context = {'show':show,'form':form})
    
    def post(self,request,show_id):

        show = Show.objects.get(pk=show_id)
        form = ShowForm(request.POST,instance=show)

        if form.is_valid():
            show = form.save()
            return redirect('show-list')

        return render(request = request,
                      template_name = 'website/show_edit.html',
                      context = {'show':show,'form':form})
    
class ShowAdd(View):
    def get(self, request):
        form = ShowForm()
        return render(request = request, 
                      template_name = 'website/show_add.html',
                      context = {'form':form})
    
    def post(self, request):
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show-list')
        return render(request = request,
                      template_name = 'website/show_add.html', 
                      context={'form': form})
    

class ShowDetails(View):
    def get(self, request, show_id):
        show = Show.objects.get(pk=show_id)
        fields = show._meta.get_fields()
        return render(request=request, 
                      template_name='website/show_detail.html', 
                      context={'show': show, 'fields':fields})

    

class ShowDelete(View):
    def get(self,request,show_id=None):

         show = Show.objects.get(pk=show_id)
         form = ShowForm(instance=show)

         return render(request = request,
                       template_name = 'website/show_delete.html',
                       context = {'show':show,'form':form})

    def post(self,request,show_id):
        show = Show.objects.get(pk=show_id)
        show.delete()
        return redirect("show-list")

class ShowListCreateView(generics.ListCreateAPIView):

    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class ShowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer

class UserListCreateView(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    