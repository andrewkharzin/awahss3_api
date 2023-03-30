# import graphene
# from graphene_django import DjangoObjectType
# from apps.directory.models.airline import Airline
# from apps.directory.models.register import Register
# from apps.directory.models.airports import Airport
# from apps.users.models import User
# from apps.profiles.models import Profile
# from django.conf import settings
# from apps.projects.schema import ScheduleType
# from apps.projects.models.flight_project import FlightProject, Tag
# from apps.payload.models import Payload

# class UserType(DjangoObjectType):
#     class Meta:
#         model = User
       

# class ProfileType(DjangoObjectType):
#     class Meta:
#         model = Profile
    
#     avatar = graphene.String()

#     def resolve_avatar(self, info):
#         if self.avatar and self.avatar.url:
#             return info.context.build_absolute_uri(self.avatar.url)

#         else:
#             return None

# # class TaskAttachType(DjangoObjectType):
# #     class Meta:
# #         model = TaskAttachments

# #     file = graphene.String()

# #     def resolve_docs(self, info):
# #         if self.file and self.file.url:
# #             return info.context.build_absolute_uri(self.file.url)

# #         else:
# #             return None

# # class DocsCategoryType(DjangoObjectType):
# #     class Meta:
# #         model = DocsCategory


# class TagType(DjangoObjectType):
#     class Meta:
#         model = Tag

# class PayloadType(DjangoObjectType):
#     class Meta:
#         model = Payload


# class ScheduleType(DjangoObjectType):
#     class Meta:
#         model = FlightProject


# class AirlineType(DjangoObjectType):
#     class Meta:
#         model = Airline

#     arl_logo = graphene.String()
#     banner_img = graphene.String()

#     # def resolve_arl_logo(self, info):
#     #   return info.context.build_absolute_uri(self.arl_logo.url)

#     def resolve_arl_logo(self, info):
#         if self.arl_logo and self.arl_logo.url:
#             return info.context.build_absolute_uri(self.arl_logo.url)

#         else:
#             return None
#     def resolve_banner_img(self, info):
#         if self.banner_img and self.banner_img.url:
#             return info.context.build_absolute_uri(self.banner_img.url)

#         else:
#             return None


# class RegistrationType(DjangoObjectType):
#     class Meta:
#         model = Register
    
#     ac_photo = graphene.String()

#     def resolve_ac_photo(self, info):
#         if self.ac_photo and self.ac_photo.url:
#             return info.context.build_absolute_uri(self.ac_photo.url)

#         else:
#             return None

# class StationType(DjangoObjectType):
#    class Meta:
#       model = Airport

#    country_flag = graphene.String()

#    def resolve_country_flag(self, info):
#         if self.country_flag and self.country_flag.url:
#             return info.context.build_absolute_uri(self.country_flag.url)

#         else:
#             return None
