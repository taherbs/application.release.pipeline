# Example release pipeline for a PHP applications

This project will work as a template for PHP microservices CI/CD.
This infrastructure could be reused for other framework different than PHP.

- **Continuous Integration** by rules develoeprs by triggering a build pipeline on a commit/merge on the master designated branch.
- **Continuous Delivery** - this is the section of the pipeline where the application archive stored in the repository from the earlier CI process is imported into a test/staging environment for further eventual regression and acceptance testing.
- **Continuous Deployment** - Here the pipeline will get deployed to the production environment.

# Notes

This is meant to be a example implementation to showcase how a continuous delivery or continuous deployment pipelines could be implemented.

- Only two environments are assumed, Staging and Production, whereas a pipeline for a real application is likely to have multiple additional stages and environments and tests. 

- This pipeline assumes that multiple arguments have been specified as entry parameters, see the section below around Docker and Sceptre configuration for more details.

- The pipeline assumes that all environments invovled are configured to be https enpoints.

This is just a starting point for your CI/CD pipelines this should be an excellent starting point to enable your teams to build a simple pipeline and grow in complexity over time.

# Prerequisites

## Tools:
- [Docker](https://docs.docker.com/)/[Docker Compose](https://docs.docker.com/compose/) - Needed to run tests localy on your machine.
- [Make](https://www.gnu.org/software/make/) - Need to be installed on Windows based systems.
- [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html)
- [sceptre](https://sceptre.cloudreach.com/latest/)

## AWS resources

- Store git personal access token in AWS parameter store
- KMS Key
- S3 Bucket for storing the build artifacts
- S3 bucket for storing ELB logs
- Service VPC
- Service application subnet(s)
- Public/ELB subnet(s)
- Route53 hosted zone
- Domain/ELB certificate

# Configuration

In order to deploy this pipeline to AWS you will need to specify the folowing entry arguments on [aws/sceptre/config/config.yaml](aws/sceptre/config/config.yaml.sample)

- project_code: A code which is prepended to the stack names of all stacks built by Sceptre.
- region: The AWS region to build stacks in. Sceptre should work in any region which supports CloudFormation.
- template_bucket_name: The name of an S3 bucket to upload CloudFormation Templates to. Note that S3 bucket names must be globally unique. If the bucket does not exist, Sceptre creates one using the given name, in the AWS region specified by region. (optional)
- template_key_prefix: A string which is prefixed onto the key used to store templates uploaded to S3
- email_team: develoeprs team email address
- git_repository: Project git repository
- git_branch: Name of the branch  to deploy
- git_token: Git deployment token path in parameters store.
- kms_key_arn: KMS Key ARN
- s3_artifacts_output_bucket: S3 bucket name for storing the build artifacts
- s3_elb_logs_bucket: S3 bucket name for storing ELB logs
- project_vpc: VPC id
- project_app_subnets: Service application subnet(s) (comma separated if multiple)
- project_public_subnets: Public/ELB subnet(s) (comma separated if multiple)
- hosted_zone_name: Route53 hosted zone name
- hosted_zone_id: Route53 hosted zone id
- project_subdomain: application subdomain name
- elb_cert: Domain/ELB certificate id
- elb_health_check_path: application healh check path
- stg_alb_policy: Load Balancer policy for staging environment
- prd_alb_policy: Load Balancer policy for production environment

# Service Deployment

## Deploy Service on your local Machine using Make, Docker and Docker Compose
```
# Deploy containers
make start-new

# Stop containers
make stop
```

## Deploy Service to AWS

Deploy the prequisites and the CI/CD  stacks

```
# Configure your aws connection
# Note that you may need to deploy stacks to multiple environments configure
# Configure your credentials accordingly
aws configure

# Enter the sceptre directory
cd aws/sceptre

# Deploy the environment
sceptre launch-env misc
sceptre launch-env ci
sceptre launch-env cd
sceptre launch-env feature/waf #(Optional - Please read the note bellow)
```

**Note:** In this project, WAF creation and association to ALB is part of the service deployment, in real use cases you will probably need to create WAF as part of the infrastructure deployment, then reuse the created WAF ID in your association.