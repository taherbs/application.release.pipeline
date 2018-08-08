"""
Retrive the value of a parameter store variabile
"""
from sceptre.resolvers import Resolver
import boto3

class GetParameter(Resolver):

    def __init__(self, *args, **kwargs):
        super(GetParameter, self).__init__(*args, **kwargs)

    def resolve(self):
        if self.argument:
            region = self.environment_config["region"]
            ssm = boto3.client(
                'ssm',
                region_name=region
            )
            response = ssm.get_parameters(
                Names=[
                    self.argument,
                ],
                WithDecryption=True
            )
            parameter = response['Parameters'][0]['Value']
            return parameter
