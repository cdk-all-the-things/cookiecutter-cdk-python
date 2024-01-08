#!/usr/bin/env python3
import os
import cdk_nag
import aws_cdk.pipelines

from aws_cdk import App, Aspects, Environment
from boto3 import client, session
from cdk_pipelines_github import AwsCredentials
from cdk.{{cookiecutter.service_name}}.stacks.service_stack import ServiceStack
from cdk.{{cookiecutter.service_name}}.utils import get_stack_name

account = client('sts').get_caller_identity()['Account']
region = session.Session().region_name
environment = os.getenv('ENVIRONMENT', 'dev')
app = App()

my_stack = ServiceStack(
    scope=app,
    id=get_stack_name(),
    env=Environment(account=os.environ.get('AWS_DEFAULT_ACCOUNT', account), region=os.environ.get('AWS_DEFAULT_REGION', region)),
    is_production_env=True if environment == 'production' else False,
)

pipeline = cdk_pipelines_github.GitHubWorkflow(
    app, 'Pipeline',
    synth=aws_cdk.pipelines.ShellStep(
        'Build',
        commands=[
            'yarn install',
            'yarn build',
        ],
    ),
    aws_creds=AwsCredentials.from_open_id_connect(
        git_hub_action_role_arn=f'arn:aws:iam::{account}:role/GitHubActionRole',
    ),
)

pipeline.add_stage(my_stack)

# Runs CDK Nag on Stack
Aspects.of(my_stack).add(cdk_nag.AwsSolutionsChecks())
app.synth()
