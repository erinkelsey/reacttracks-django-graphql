import graphene
from graphene_django import DjangoObjectType

from .models import Track

class TrackType(DjangoObjectType):
  class Meta:
    model = Track


class Query(graphene.ObjectType):
  tracks = graphene.List(TrackType)

  def resolve_tracks(self, info):
    return Track.objects.all()

# {
#   tracks {
#     id 
#     title
#     description
#     createdAt
#   }
# }

class CreateTrack(graphene.Mutation):
  track = graphene.Field(TrackType)

  class Arguments:
    title = graphene.String()
    description = graphene.String()
    url = graphene.String()

  # def mutate(self, info, **kwargs):
  #   kwargs.get('title')
  def mutate(self, info, title, description, url):
    track = Track(title=title, description=description, url=url)
    track.save()

    return CreateTrack(track=track)


class Mutation(graphene.ObjectType):
  create_track = CreateTrack.Field()

# mutation {
#   createTrack(title: "Track 3", description: "Track 3 description", url: "https://track3.com"){
#     track {
#       id
#       title
#       description
#       url
#       createdAt
#     }
#   }
# }