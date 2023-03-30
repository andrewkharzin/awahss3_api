# import graphene
# from .types import *
# from apps.directory.models.airline import Airline
# from apps.directory.models.register import Register
# from apps.directory.models.airports import Airport
# from apps.users.models import User
# from apps.profiles.models import Profile
# from django.conf import settings
# from apps.projects.schema import ScheduleType
# from apps.projects.models.flight_project import FlightProject, Tag
# from apps.payload.models import Payload




# class Query(graphene.ObjectType):
#     get_user_profile = graphene.List(ProfileType)
#     get_users = graphene.List(UserType)
#     all_airlines = graphene.List(AirlineType)
#     get_registers = graphene.List(RegistrationType)
#     all_flights = graphene.List(ScheduleType)
#     get_taskTags = graphene.List(TagType)
#     get_stations = graphene.List(StationType)
#     get_payload = graphene.List(PayloadType)
#     # get_flights_task_docs = graphene.List(TaskAttachType)

#     # JKNK------>>>>
#     get_task_by_id = graphene.Field(ScheduleType, pkid=graphene.String())

#     def resolve_get_users(root, info):
#         return (
#             User.objects.all()
#         )
#     def resolve_get_user_profile(root, info):
#         return (
#             Profile.objects.all()
#         )
#     def resolve_all_airlines(root, info):
#         return (
#             Airline.objects.all()
#         )

#     def resolve_get_registers(root, info):
#         return (
#             Register.objects.all()
#         )
#     def resolve_all_flights(root, info):
#         return (
#             FlightProject.objects.all()
#         )
#     def resolve_get_stations(root, info):
#         return (
#             Airport.objects.all()
#         )
#     def resolve_get_payload(root, info):
#         return (
#             Payload.objects.all()
#         )
#     def resolve_get_taskTags(root, info):
#         return (
#             Tag.objects.all()
#         )
#     # def resolve_get_flights_task_docs(root, info):
#     #     return (
#     #         TaskAttachments.objects.all()
#     #     )

#     def resolve_get_task_by_id(root, info, pkid):
#         return (
#             FlightProject.objects.get(pk=pkid)
#         )
