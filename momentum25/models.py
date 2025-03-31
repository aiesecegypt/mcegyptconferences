from django.db import models
from django.utils.crypto import get_random_string


class Delegate(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)

    role = models.CharField(max_length=50)
    function = models.CharField(max_length=50)
    lc = models.CharField(max_length=100)
    lc_password = models.CharField(max_length=100)

    allergies = models.CharField(max_length=10)
    allergy_details = models.TextField(blank=True, null=True)

    tshirt_size = models.CharField(max_length=5)
    tshirt_quantity = models.PositiveIntegerField(default=0)

    agree_policy = models.BooleanField(default=False)

    # 🧾 File fields for uploads
    id_front = models.FileField(upload_to='uploads/id_front/', blank=True, null=True)
    id_back = models.FileField(upload_to='uploads/id_back/', blank=True, null=True)
    indemnity_form = models.FileField(upload_to='uploads/indemnity_forms/', blank=True, null=True)

    delegate_id = models.CharField(max_length=20, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.delegate_id:
            self.delegate_id = self._generate_delegate_id()
        super(Delegate, self).save(*args, **kwargs)

    def _generate_delegate_id(self):
        lc_codes = {
            "6th October University": "6OU", "AAST Alexandria": "AASTA", "AAST In CAIRO": "AASTC",
            "Ain Shams University": "ASU", "Alexandria": "ALX", "AUC": "AUC", "Beni Suef": "BSF",
            "Cairo University": "CU", "Galala": "GAL", "GUC": "GUC", "Helwan": "HEL", "Mansoura": "MAN",
            "Menofia": "MEN", "MIU": "MIU", "MSA": "MSA", "MUST": "MUST", "New Capital": "NCAP",
            "Suez": "SUZ", "Tanta": "TAN", "Zagazig": "ZAG"
        }

        prefix = lc_codes.get(self.lc, "LCX")

        # Count existing delegates with the same LC
        count = Delegate.objects.filter(lc=self.lc).count() + 1
        number = str(count).zfill(3)  # pad with zeros to 3 digits

        return f"{prefix}-{number}"

    def __str__(self):
        return f"{self.full_name} - {self.delegate_id}"
