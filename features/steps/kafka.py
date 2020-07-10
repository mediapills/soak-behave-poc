from behave import given, when, then
import subprocess


def get_process(cmd):
    return subprocess.Popen(
        cmd.strip().split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True)


@when('create a new topic {name}')
def setup_service(context, name):
    cmd = 'dcos kafka topic create {}'.format(name)

    process = get_process(cmd)
    stdout, stderr = process.communicate()

    print(stderr)
    assert stderr == b''
    context.topic_created = True


@then('behave will test kafka for us!')
def step_impl(context):
    assert context.failed is False
    assert context.topic_created is True
