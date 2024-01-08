from aws_cdk import App
from aws_cdk.assertions import Template

from cdk.{{cookiecutter.service_name}}.stacks.service_stack import ServiceStack


def test_synthesizes_properly():
    app = App()

    service_stack = ServiceStack(app, 'service-test', is_production_env=True)

    # Prepare the stack for assertions.
    template = Template.from_stack(service_stack)
