from django.http import HttpResponseRedirect
from django.views.generic.detail import SingleObjectMixin
from django.views.generic import ListView
from circon.sales.sale.models import Sale
from circon.sales.sale.models import SaleDetail
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from pure_pagination.mixins import PaginationMixin
from .forms import SaleForm
from .forms import SaleFormSet
from .forms import SaleDetailForm
from extra_views import UpdateWithInlinesView
from extra_views import InlineFormSet


class ListExit(PaginationMixin, ListView):
    template_name = 'warehouse/exit/list.html'
    model = Sale
    paginate_by = 10


class DetailExitDetail(SingleObjectMixin, ListView):
    template_name = 'warehouse/exit/detail.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Sale.objects.all())
        return super(DetailExitDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DetailExitDetail, self).get_context_data(**kwargs)
        context['sale'] = self.object
        return context

    def get_queryset(self):
        return self.object.saledetail_set.all()


class CreateExit(CreateView):
    template_name = 'warehouse/exit/create.html'
    model = Sale
    form_class = SaleForm
    success_url = '/List_Exit'

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sale_form = SaleFormSet()
        return self.render_to_response(
               self.get_context_data(form=form,
                                     sale_form=sale_form,))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        sale_form = SaleFormSet(self.request.POST)
        if (form.is_valid() and sale_form.is_valid()):
            return self.form_valid(form, sale_form)
        else:
            return self.form_invalid(form, sale_form)

    def form_valid(self, form, sale_form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.status = '0'
        self.object = form.save()

        sale_form.instance = self.object
        sale_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, sale_form):
        return self.render_to_response(
               self.get_context_data(form=form,
                                     sale_form=sale_form,))


class ItemInline(InlineFormSet):
    model = SaleDetail
    form_class = SaleDetailForm


class UpdateExit(UpdateWithInlinesView):
    template_name = 'warehouse/exit/update.html'
    model = Sale
    inlines = [ItemInline]

    def get_success_url(self):
        return reverse('detail_exit', kwargs={'pk': self.object.pk})


class DeleteExit(DeleteView):
    template_name = 'warehouse/exit/delete.html'
    model = Sale
    success_url = reverse_lazy('list_exit')


class Confirm(UpdateView):
    template_name = 'warehouse/exit/confirm.html'
    model = Sale
    fields = ['status']
    initial = {'status': '1'}

    def get_success_url(self):
        return reverse('detail_exit', kwargs={'pk': self.object.pk})


class Delivered(UpdateView):
    template_name = 'warehouse/exit/delivered.html'
    model = Sale
    fields = ['status']
    initial = {'status': '1'}

    def get_success_url(self):
        return reverse('detail_exit', kwargs={'pk': self.object.pk})


class Cancel(UpdateView):
    template_name = 'warehouse/exit/cancel.html'
    model = Sale
    fields = ['status']
    initial = {'status': '3'}

    def get_success_url(self):
        return reverse('detail_exit', kwargs={'pk': self.object.pk})
