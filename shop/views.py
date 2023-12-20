from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.views import View
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models

# Create your views here.
# class ShopDetailView(View):
#     def get(self, request:HttpRequest, pk:int) -> HttpResponse:
#         course = get_object_or_404(models.Course, pk=pk)
#         return render(request, 'shop/shop_item.html', {'course': course})
    
class ShopDetailView(LoginRequiredMixin,DetailView):
    template_name = 'shop/shop_item.html'
    model = models.Course
    context_object_name = 'course'

# class shopItems(TemplateView):
#     template_name = 'shop/courses.html'

#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context['courses'] = models.Course.objects.all().select_related("Category")
#         #Courses = get_object_or_404(models.Course)
#         #context = {
#             #'courses': Courses
#         #}
#         return context 


class shopItems(ListView):
    template_name = 'shop/courses.html'
    model = models.Course
    context_object_name = 'courses'
    queryset = models.Course.objects.filter(archived = False)


class OrderDetail(PermissionRequiredMixin,DetailView):
    permission_required = 'shop.view_order'
    template_name = 'shop/orders.html'
    queryset = (models.Order.objects.select_related('user').prefetch_related('coursetype'))
    model = models.Order


class shopCreate(CreateView):
    template_name = 'shop/create_items.html'
    model = models.Course
    fields = 'title', 'price','check_qty', 'reviews_qty','Category'
    success_url = reverse_lazy('shop:index')

class shopitemupdate(UpdateView):
    template_name = 'shop/update_items.html'
    model = models.Course
    fields = 'title', 'price','check_qty', 'reviews_qty','Category','archived','about'
    success_url = reverse_lazy('shop:shop_item')
    def get_success_url(self):
        return reverse(
            'shop:shop_item',
            kwargs={'pk': self.object.pk}
        )
    

class ShopItemDelete(DeleteView):
    model = models.Course
    success_url = reverse_lazy('shop:index')
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    


# class ShopIndexView(View):
#     def get(self,request):
#         Courses = models.Course.objects.all().select_related('Category')
#         #return HttpResponse(''.join([str(courses) + '<br>' for courses in Courses]))
#         return render(request, 'shop/courses.html', {'courses':Courses})
# def index(request):
#     Courses = models.Course.objects.all().select_related('Category')
#     #return HttpResponse(''.join([str(courses) + '<br>' for courses in Courses]))
#     return render(request, 'shop/courses.html', {'courses':Courses})

# def shop_item(request, item_id):
#     # try:
#     #     course = models.Course.objects.get(id = item_id)
#     #     return render(request, 'shop_item.html', {'course': course})
#     # except models.Course.DoesNotExist:
#     #     raise Http404()
#     course = get_object_or_404(models.Course, id = item_id)
#     return render(request, 'shop/shop_item.html', {'course': course})
