from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    # =========================
    # 🔹 IDENTIFIANT LOGIN
    # =========================
    # email = models.EmailField(unique=True)
    email = models.EmailField(unique=True, max_length=191)


    # =========================
    # 🔹 INFOS UTILISATEUR
    # =========================
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    phone = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to="users/", null=True, blank=True)

    # =========================
    # 🔹 STATUT COMPTE
    # =========================
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    # =========================
    # 🔹 CONFIG AUTHENTIFICATION
    # =========================
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["first_name", "last_name"]

    # lien avec manager
    objects = UserManager()

    # =========================
    # 🔹 AFFICHAGE OBJET
    # =========================
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    # optionnel (très utile)
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name