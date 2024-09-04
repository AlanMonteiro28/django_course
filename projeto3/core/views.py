from typing import Any
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Feature
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        half_index = self.get_feature_half_index()
        
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('id').all()
        context['funcionarios'] = Funcionario.objects.order_by('id').all()
        context['features_left'] = Feature.objects.order_by('id')[:half_index]
        context['features_right'] = Feature.objects.order_by('id')[half_index:]

        return context
    
    def get_feature_half_index(self, total_features=None):
        if total_features is None:
            total_features = Feature.objects.count()
        features_half_i = total_features // 2 #calcula a metade do total das features para definir left e right da formataçao

        return features_half_i

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso.')

        return super(IndexView, self).form_valid(form, *args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail.')
        
        return super(IndexView, self).form_invalid(form, *args, **kwargs)