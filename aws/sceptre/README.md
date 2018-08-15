# devops.pipeline aws infrastructure deployment

This directory defines multiple cloudformation templates for setting up the CI/CD infrastructure on AWS.<br />

### Auto Stacks deployment and configuration
Deploy the prequisites and the CI/CD  stacks
```
# Configure your aws connection
# Note that you may need to deploy stacks to multiple environments configure
# Configure your credentials accordingly
aws configure

# Enter the sceptre directory
cd sceptre

# Deploy the environment
sceptre launch-env misc
sceptre launch-env ci
sceptre launch-env cd
sceptre launch-env feature/waf
```

### Other Sceptre useful commands
Find bellow some useful sceptre commands:
```
# Deploy only the STG stacks
sceptre launch-env cd/stg

# Deletes the service STG stacks:
sceptre delete-env cd/stg

# Validate stack template, example: 
sceptre validate-template cd/stg/net alb
```
