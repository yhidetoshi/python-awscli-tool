
import click
import boto3
import json

@click.group(help='Subcommand click CLI') # (1)
@click.option('-p', '--profile', type=str)
@click.pass_context
def main(ctx, profile):
    ctx.params['session'] = boto3.session.Session(profile_name=ctx.params.get('profile'))

@main.group(help='EC2 API') # (2)
@click.pass_context
def ec2(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('ec2')

# EC2 List
@ec2.command(help='EC2 DescribeInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def describe_instances(ctx, instance_id):
    instance_ids = [instance_id] if instance_id else []
#    print(json.dumps(list(ctx.parent.params['client'].describe_instances(InstanceIds=instance_ids))))
    print(ctx.parent.params['client'].describe_instances(InstanceIds=instance_ids))

# EC2 start
@ec2.command(help='EC2 RunInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def start_instances(ctx, instance_id):
    instance_ids = [instance_id]
    try:
        ctx.parent.params['client'].start_instances(InstanceIds=instance_ids)
        print('Start Success')
    except:
        print('Error')

    print('Finish')

# EC2 stop
@ec2.command(help='EC2 RunInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def stop_instances(ctx, instance_id):
    instance_ids = [instance_id]
    try:
        ctx.parent.params['client'].stop_instances(InstanceIds=instance_ids)
        print('Stop Success')
    except:
        print('Error')

    print('Finish')

if __name__ == '__main__':
    main()
