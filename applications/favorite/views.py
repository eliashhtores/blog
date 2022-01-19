from django.views.generic import View, DeleteView
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Favorite
from applications.entry.models import Entry


class AddFavoriteView(LoginRequiredMixin, View):
    login_url = reverse_lazy("users_app:login")

    def post(self, request, *args, **kwargs):
        entry = Entry.objects.get(id=self.kwargs['pk'])
        Favorite.objects.create(user=self.request.user, entry=entry)
        return redirect(reverse("users_app:panel"))


class DeleteFavoriteView(DeleteView):
    model = Favorite
    success_url = reverse_lazy("users_app:panel")
