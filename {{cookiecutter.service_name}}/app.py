#!/usr/bin/env python3
import os
import aws_cdk.pipelines

from aws_cdk import App, Aws
from cdk_pipelines_github import AwsCredentials, GitHubWorkflow

from cdk.{{cookiecutter.service_name}}.pipeline.service_stage import ServiceStage
from cdk.{{cookiecutter.service_name}}.pipeline.setup_stage import SetupStage

account = Aws.ACCOUNT_ID
region = Aws.REGION
environment = os.getenv('ENVIRONMENT', 'dev')
app = App()

pipeline = GitHubWorkflow(
    app, 'Pipeline',
    synth=aws_cdk.pipelines.ShellStep(
        'Build',
        commands=[
            'yarn install',
            'make dev',
        ],
    ),
    aws_creds=AwsCredentials.from_open_id_connect(
        git_hub_action_role_arn=f'arn:aws:iam::{account}:role/GitHubActionRole',
    ),
)

setup_stage = SetupStage(
    scope=app,
    id='setup-stage')

dev_stage = ServiceStage(
    scope=app,
    id='dev-service-stage'
)

pipeline.add_stage(setup_stage)
devWave = pipeline.add_wave('Development')
devWave.add_stage(dev_stage)

app.synth()
