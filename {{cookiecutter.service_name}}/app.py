#!/usr/bin/env python3
import os
import aws_cdk.pipelines

from aws_cdk import App, Aws
from cdk_pipelines_github import AwsCredentials, GitHubWorkflow

from cdk.{{cookiecutter.service_name}}.stacks.service_stack import ServiceStack

account = Aws.ACCOUNT_ID
region = Aws.REGION
environment = os.getenv('ENVIRONMENT', 'dev')
app = App()


app.synth()
