"""
Delete all images from designated Ecr repository
"""

from sceptre.hooks import Hook
import boto3

class CleanEcrRepo(Hook):

    def __init__(self, *args, **kwargs):
        super(CleanEcrRepo, self).__init__(*args, **kwargs)

    def run(self):
        if self.argument:
            region = self.environment_config["region"]
            repository_name = self.argument
            client = boto3.client('ecr', region_name=region)
        
            # Get repository images ID
            response = client.describe_images(repositoryName=repository_name)
            imageIds = []
            for imageDetail in response['imageDetails']:
                imageIds.append(
                    {
                        'imageDigest': imageDetail['imageDigest'],
                    }
                )
            # Delete images if exist
            if not len(imageIds):
                print('No images to delete.')
            else:
                print('Starting images deletion...')
                response = client.batch_delete_image(
                    repositoryName=repository_name,
                    imageIds=imageIds
                )
                print(response)
        else:
            raise "Error - Expected Ecr Repository name argument."