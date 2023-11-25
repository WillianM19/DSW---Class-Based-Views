from django.shortcuts import render
from django.urls import reverse_lazy
from hospedagem.models import Hospedagem
from hospedagem.forms import HospedagemForm
from django.views.generic import DetailView,UpdateView,CreateView,DeleteView,ListView

# Create your views here.
class CriarHospedagem(CreateView):
    template_name = 'criarHospedagem.html'
    form_class = HospedagemForm
    success_url = reverse_lazy('ListarHospedagem')

class ListarHospedagem(ListView):
    model = Hospedagem
    template_name = 'listarHospedagem.html'
    context_object_name = 'hospedagens' 

class EditarHospedagem(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'editarHospedagem.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('ListarHospedagem')

class DetalheHospedagem(DetailView):
    model = Hospedagem
    template_name = "detalheHospedagem.html"
    context_object_name = "hospedagem"
    pk_url_kwarg = 'id'


class ExcluirHospedagem(DeleteView):
    model = Hospedagem
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('ListarHospedagem')
    
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)