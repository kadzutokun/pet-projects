from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import FormMixin
from . import models
from .forms import CommentForm

# Create your views here.
# class ShopDetailView(View):
#     def get(self, request:HttpRequest, pk:int) -> HttpResponse:
#         course = get_object_or_404(models.Course, pk=pk)
#         return render(request, 'shop/shop_item.html', {'course': course})
    
class ShopDetailView(LoginRequiredMixin,DetailView, CreateView):
    template_name = 'shop/shop_item.html'
    model = models.Course
    context_object_name = 'course'
    form_class = CommentForm


    # Отрисовывание комментариев
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.filter(coursecom=self.kwargs['pk']) 
        return context
    

    def post(self, request, *args, **kwargs):
        course = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.coursecom = course
            comment.commenttext = form.cleaned_data['commenttext']
            comment.save()
            return redirect('shop:shop_item', pk=course.pk)
        else:
            context = self.get_context_data(object=self.object)
            context['comment_form'] = form
            return self.render_to_response(context)
    
        
    def get_success_url(self):
        return reverse(
            'shop:shop_item',
            kwargs={'pk': self.object.pk}
        )

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


class CommentCreate(CreateView):
    template_name = 'shop/shop_item.html'
    model = models.Comment
    fields = 'commenttext', 
    success_url = reverse_lazy('shop:index')


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

class CommentDelete(DeleteView):
    model = models.Comment
    success_url = reverse_lazy('shop:index')
    def CommentDelete(request):
        comment = models.Comment.objects.all()
        if comment.user == request.user:
            comment.is_removed == True
            comment.save()
        return reverse_lazy('shop:index')




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
