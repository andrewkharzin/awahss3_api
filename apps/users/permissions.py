from django.contrib.auth.models import Permission

NOT_AUTHORIZED_PERMISSIONS = [
    Permission.objects.get(codename='view_order'),
]

AGENT_PERMISSIONS = [
    Permission.objects.get(codename='add_order'),
    Permission.objects.get(codename='change_order'),
    Permission.objects.get(codename='delete_order'),
]

ACCOUNT_PERMISSIONS = [
    Permission.objects.get(codename='view_order'),
    Permission.objects.get(codename='change_order_status'),
]

SHIFTLEADER_PERMISSIONS = [
    Permission.objects.get(codename='view_order'),
    Permission.objects.get(codename='change_order_status'),
]

MANAGER_PERMISSIONS = [
    Permission.objects.get(codename='view_order'),
    Permission.objects.get(codename='add_user'),
    Permission.objects.get(codename='change_user'),
    Permission.objects.get(codename='delete_user'),
]

