
import click
import boto3
import json
from prettytable import PrettyTable

@click.group(help='Subcommand click CLI')
@click.option('-p', '--profile', type=str)
@click.pass_context
def main(ctx, profile):
    ctx.params['session'] = boto3.session.Session(profile_name=ctx.params.get('profile'))

@main.group(help='EC2 API')
@click.pass_context
def ec2(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('ec2')

# EC2 List
@ec2.command(help='EC2 DescribeInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def describe_instances(ctx, instance_id):
    table = PrettyTable(['InstanceName', 'InstanceId', 'InstanceType'])
    table.align['InstanceName'] = 'l'
    table.align['InstanceId'] = 'l'
    table.align['InstanceType'] = 'l'
    response=[]
    instance_ids = [instance_id] if instance_id else []
    response = ctx.parent.params['client'].describe_instances(InstanceIds=instance_ids)
    instance_count = len(response['Reservations'])

    for i in range(0, instance_count):
        table.add_row([
                       response['Reservations'][i]['Instances'][0]['Tags'][0]['Value'],
                       response['Reservations'][i]['Instances'][0]['InstanceId'],
                       response['Reservations'][i]['Instances'][0]['InstanceType'],
                      ])
    print (table)

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
@ec2.command(help='EC2 StopInstances API')
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

# AMI List
@ec2.command(help='Amazon Linux Image List API')
@click.pass_context
def describe_ami(ctx):
    images=[]
    sorted_ami=[]
    table = PrettyTable(['ImageName','CreateDate'])
    table.align['ImageName'] = 'l'
    table.align['CreateDate'] = 'l'
    try:
        images = ctx.parent.params['client'].describe_images(Owners=["self"])["Images"]
        for ami in sorted(images, key = lambda x:x['CreationDate']):
            sorted_ami.append(ami)

        for i in range(0, len(sorted_ami)):
            table.add_row([sorted_ami[i]['Name'],sorted_ami[i]['CreationDate']])
        print(table)
    except:
        print('Error')
    print('Finish')

if __name__ == '__main__':
    main()
