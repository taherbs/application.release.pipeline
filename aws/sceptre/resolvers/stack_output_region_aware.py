"""
Retrive stacks output from a different region than the source.
"""
from sceptre.resolvers.stack_output import StackOutput
from sceptre.environment import Environment
from sceptre.resolvers import Resolver
import boto3

class StackOutputRegionAware(StackOutput):

    def __init__(self, *args, **kwargs):
        super(StackOutputRegionAware, self).__init__(*args, **kwargs)

    def resolve(self):
        if self.argument:
            source_stack_path = self.dependency_stack_name
            source_env_path, source_stack_name = source_stack_path.rsplit('/', 1)
            environment = Environment(self.environment_config.sceptre_dir, source_env_path)
            source_stack = environment.stacks[source_stack_name] 
            region = source_stack.region
            source_stack_full_name = "-".join([
                self.environment_config["project_code"],
                self.dependency_stack_name.replace("/", "-")
            ])
            output_key = self.argument.split("::")[1]
            
            cloudformation = boto3.client(
                'cloudformation',
                region_name=region
            )
            response = cloudformation.describe_stacks(
                StackName=source_stack_full_name
            )
            for output in response["Stacks"][0]["Outputs"]:
                if (output["OutputKey"] == output_key):
                    return output["OutputValue"]
            raise Exception("could not retrieve '{}' output value from '{}' stack").format(output_key, source_stack_path)