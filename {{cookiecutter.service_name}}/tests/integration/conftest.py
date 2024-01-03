import os

import pytest

from cdk.{{cookiecutter.service_name}}.constants import (
    CONFIGURATION_NAME,
    ENVIRONMENT,
    POWER_TOOLS_LOG_LEVEL,
    POWERTOOLS_SERVICE_NAME,
    SERVICE_NAME,
)
from tests.utils import get_stack_output


@pytest.fixture(scope='module', autouse=True)
def init():
    os.environ[POWERTOOLS_SERVICE_NAME] = SERVICE_NAME
    os.environ[POWER_TOOLS_LOG_LEVEL] = 'DEBUG'
    os.environ['ROLE_ARN'] = 'arn:partition:service:region:account-id:resource-type:resource-id'
    os.environ['CONFIGURATION_APP'] = SERVICE_NAME
    os.environ['CONFIGURATION_ENV'] = ENVIRONMENT
    os.environ['CONFIGURATION_NAME'] = CONFIGURATION_NAME
    os.environ['CONFIGURATION_MAX_AGE_MINUTES'] = '5'
    os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'  # used for appconfig mocked boto calls

