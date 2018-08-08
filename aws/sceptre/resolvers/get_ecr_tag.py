"""
Retrive the value of a ecr repositories tags
"""
from sceptre.resolvers import Resolver
import boto3

class GetEcrTag(Resolver):

    def __init__(self, *args, **kwargs):
        super(GetEcrTag, self).__init__(*args, **kwargs)

    def resolve(self):
        if self.argument:
            region = self.environment_config["region"]
            client = boto3.client('ecr', region_name=region)
            response = client.describe_images(
                repositoryName=self.argument,
                imageIds=[
                    {
                        'imageTag': 'latest'
                    }
                ]
            )
            image = response['imageDetails'][0]
            tags = image['imageTags']
            tag = [elem for elem in tags if elem != "latest"]
            if not tag:
                tag = 'latest'
            return tag[0]
