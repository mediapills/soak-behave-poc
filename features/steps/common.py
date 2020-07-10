from behave import given, when, then
from shutil import which
import subprocess


def get_process(cmd):
    return subprocess.Popen(
        cmd.strip().split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)


@given('we have {app} installed')
def step_impl(context, app):
    assert which(app) is not None


@when('can execute {cmd} without issue')
def execute_successfully(context, cmd):
    process = get_process(cmd)
    stdout, stderr = process.communicate()

    assert stderr == b''
    context.cluster_exists = True


@when('install the {name} package')
def setup_service(context, name):
    cmd = 'dcos package install {}'.format(name)

    process = get_process(cmd)
    stdout, stderr = process.communicate()

    print(stderr)
    assert stderr == b''
    context.service_exists = True


@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    # assert context.cluster_exists is True



