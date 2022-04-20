from django.db import models
from apps.sites.models import EpaSite

# Choices
STATUS = [
    ('notAssigned', 'Not Assigned'),
    ('Pending', 'Pending'),
    ('Scheduled', 'Scheduled'),
    ('InTransit', 'In Transit'),
    ('ReadyForSignature', 'Ready for Signature'),
    ('Signed', 'Signed'),
    ('Corrected', 'Corrected'),
    ('UnderCorrection', 'Under Correction'),
    ('MtnValidationFailed', 'MTN Validation Failed'),
]

SUB_TYPE = [
    ('FullElectronic', 'Full Electronic'),
    ('DataImage5Copy', 'Data + Image'),
    ('Hybrid', 'Hybrid'),
    ('Image', 'Image'),
]

ORIGIN_TYPE = [
    ('Web', 'Web'),
    ('Service', 'Service'),
    ('Mail', 'Mail'),
]


class Manifest(models.Model):
    # see documentation on USEPA/e-Manifest repo
    # https://github.com/USEPA/e-manifest/blob/master/Services-Information/Schema/emanifest.json
    created_date = models.DateTimeField('created date', auto_now_add=True)
    update_date = models.DateTimeField('update date', auto_now_add=True)
    manifest_tracking_number = models.CharField(max_length=15)
    status = models.CharField(max_length=25,
                              choices=STATUS,
                              default='notAssigned')
    submission_type = models.CharField(max_length=25,
                                       choices=SUB_TYPE,
                                       default='FullElectronic')
    origin_type = models.CharField(max_length=25,
                                   choices=ORIGIN_TYPE,
                                   default='Service')
    shipped_date = models.DateTimeField('shipped date', null=True)
    potential_ship_date = models.CharField(max_length=15, null=True)
    received_date = models.DateTimeField('received date', null=True)
    certified_date = models.DateTimeField('certified date', null=True)
    # Hazardous waste handlers
    transporter = models.JSONField()
    generator_id = models.CharField(max_length=25)
    generator_info = models.JSONField()
    tsd_id = models.CharField(max_length=25)
    tsd_info = models.JSONField()
    rejection = models.BooleanField(default=False)
    residue = models.BooleanField(default=False)
    import_waste = models.BooleanField(default=False)
    contains_rejected_residue = models.BooleanField(default=False)

    def __str__(self):
        return self.manifest_tracking_number


class ElectronicSignature(models.Model):
    signer_first_name = models.CharField(max_length=200)
    signer_last_name = models.CharField(max_length=200)
    signer_user_id = models.CharField(max_length=200)
    signature_date = models.DateTimeField('signature_date')

    def __str__(self):
        return f'{self.signature_date} by {self.signer_user_id}'