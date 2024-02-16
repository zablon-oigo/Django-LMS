from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Course
from django.views.generic.base import TemplateResponseMixin,View
from .forms import ModuleFormSet

class OwnerMixin:
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(owner=self.request.user)
    
class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner=self.request.user

        return super().form_valid(form)
    

class OwnerCourseMixin(OwnerMixin,LoginRequiredMixin,PermissionRequiredMixin):
    model =Course
    fields=['subject','title','slug','overview']

    success_url=reverse_lazy('manage_course_list')

class OwnerCourseEditMixin(OwnerCourseMixin,OwnerEditMixin):
    template_name='course/form.html'


class ManageCourseListView(OwnerCourseMixin,ListView):
    template_name='course/list.html'
    permission_required='course.view_course'

class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required='course.view_course'

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required='course.view_course'

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name='course/delete.html'
    permission_required='course.view_course'

class CourseModuleUpdateView(TemplateResponseMixin, View):
    template_name='course/module/formset.html'
    course=None

    def get_formset(self, data=None):
        return ModuleFormSet(instance=self.course, data=data)
    
    def dispatch(self, request, pk):
        self.course = get_object_or_404(Course,id=pk, owner=request.user)

        return super().dispatch(request, pk)
    
    def get(self, request, *args, **kwargs):
        formset=self.get_formset()
        return self.render_to_response({
            'course':self.course,
            'formset':formset
        })
    
    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)

        if formset.is_valid():
            formset.save()
            return redirect('manage_course_list')
        return self.render_to_response({
            'course':self.course,
            'formset':formset
        })