from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    # =========================
    # 🔹 CRÉER UTILISATEUR NORMAL
    # =========================
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):

        # Vérifie email obligatoire
        if not email:
            raise ValueError("Email is required")

        # Normalise email
        email = self.normalize_email(email)

        # Création user
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )

        # Hash password (IMPORTANT sécurité)
        user.set_password(password)

        # Sauvegarde en base
        user.save(using=self._db)

        return user

    # =========================
    # 🔹 CRÉER SUPER USER (ADMIN)
    # =========================
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):

        # Permissions admin obligatoires
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        # Sécurité validation
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        # Appelle create_user
        return self.create_user(email, first_name, last_name, password, **extra_fields)