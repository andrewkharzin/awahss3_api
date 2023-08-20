from django.db.models.signals import post_save
from apps.users.profile.profile import Profile
from apps.users.models import User
# from apps.agents.models.agent import Agent
# from apps.organizations.models import Organization
from django.dispatch import receiver
# from apps.agents.models.company import Company


# Auto add Agent
# @receiver(post_save, sender=Profile)
# def create_profile_agentid(sender, instance, created, **kwargs):
#     if created:
#         Agent.objects.create(profile=instance)

# @receiver(post_save, sender=Profile)
# def save_profile_agentid(sender, instance, **kwargs):
#     instance.agent.save()



# @receiver(post_save, sender=Profile)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Company.objects.create(profile=instance)


# @receiver(post_save, sender=Profile)
# def save_user_profile(sender, instance, **kwargs):
#     instance.company.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
