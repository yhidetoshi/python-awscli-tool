#! /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import boto3
import json

## importモジュール(./Modules/に関数を実装) ##
import Modules

## CLI Profile ##
@click.group(help='Subcommand click CLI')
@click.option('-p', '--profile', type=str)
@click.pass_context
#def main(ctx, profile):
def cli(ctx, profile):
    ctx.params['session'] = boto3.session.Session(profile_name=ctx.params.get('profile'))

######################
##  Create Session  ##
######################

## EC2 ##
@cli.group(help='EC2 API')
@click.pass_context
def ec2(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('ec2')

## S3 ##
@cli.group(help='S3 API')
@click.pass_context
def s3(ctx):
    ctx.params['client'] = ctx.parent.params['session'].resource('s3')

## AutoScaling ##
@cli.group(help='AutoScaling API')
@click.pass_context
def asg(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('autoscaling')

## Route53 ##
@cli.group(help='Route53 API')
@click.pass_context
def route53(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('route53')

## RDS ##
@cli.group(help='RDS API')
@click.pass_context
def rds(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('rds')


######################
##   EC2 Instance   ##
######################

## EC2 List ##
@ec2.command(help='EC2 DescribeInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def describe_instances(ctx, instance_id):
    Modules.ec2.describe_instances(ctx, instance_id)

## EC2 start ##
@ec2.command(help='EC2 RunInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def start_instances(ctx, instance_id):
    Modules.ec2.start_instances(ctx, instance_id)

## EC2 stop ##
@ec2.command(help='EC2 StopInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def stop_instances(ctx, instance_id):
    Modules.ec2.stop_instances(ctx, instance_id)

## EC2 terminate ##
@ec2.command(help='EC2 TerminateInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def terminate_instances(ctx, instance_id):
    Modules.ec2.ter_instances(ctx, instance_id)


## AMI List ##
@ec2.command(help='Amazon Linux Image List API')
@click.pass_context
def describe_ami(ctx):
    Modules.ec2.describe_ami(ctx)

## AMI CreateAMI ##
@ec2.command(help='Amazon Linux Image Create API')
@click.option('--instance-id', type=str, help='input instanceid')
@click.option('--aminame', type=str, help='input aminame')
@click.pass_context
def create_ami(ctx, instance_id, aminame):
    Modules.ec2.create_ami(ctx, instance_id, aminame)

## AMI DeleteAMI ##
@ec2.command(help='Amazon Linux Image Delete API')
@click.option('--imageid', type=str, help='input imageid')
@click.pass_context
def delete_ami(ctx, imageid):
    Modules.ec2.delete_ami(ctx, imageid)

######################
##    RDS   ##
######################

## RDSインスタンス一覧 ##
@rds.command(help='RDS RunInstances describe API')
@click.pass_context
def describe_instances(ctx):
    Modules.rds.describe_instances(ctx)

## RDS start ##
@rds.command(help='RDS RunInstances start API')
@click.option('--name', type=str, help='specify instance id')
@click.pass_context
def start_instances(ctx, name):
    Modules.rds.start_instances(ctx, name)

## RDS stop ##
@rds.command(help='RDS RunInstances stop API')
@click.option('--name', type=str, help='specify instance id')
@click.pass_context
def stop_instances(ctx, name):
    Modules.rds.stop_instances(ctx, name)


######################
##    AutoScaling   ##
######################

## AutoScaling(Describe) ##
@asg.command(help='AutoScaling Describe API')
#@click.option('--asg_name', type=str, help='input as name')
@click.pass_context
def describe_asg(ctx):
    Modules.autoscaling.describe_asg(ctx)

## AutoScaling(Update Max) ##
@asg.command(help='AutoScaling Update Max API')
@click.option('--asgname', type=str, help='update asgname')
@click.option('--max', type=int, help='update max')
@click.pass_context
def update_max(ctx, asgname, max):
    Modules.autoscaling.update_max(ctx, asgname, max)

## AutoScaling(Update Min) ##
@asg.command(help='AutoScaling Update Min API')
@click.option('--asgname', type=str, help='update asgname')
@click.option('--min', type=int, help='update min')
@click.pass_context
def update_min(ctx, asgname, min):
    Modules.autoscaling.update_min(ctx, asgname, min)

## AutoScaling(Update Desire) ##
@asg.command(help='AutoScaling Update Desire API')
@click.option('--asgname', type=str, help='update asgname')
@click.option('--desire', type=int, help='update desire')
@click.pass_context
def update_desire(ctx, asgname, desire):
    Modules.autoscaling.update_desire(ctx, asgname, desire)

######################
##     Route53      ##
######################

## Route53 List Zones ##
@route53.command(help='Route53 API')
@click.pass_context
def describe_zones(ctx):
    Modules.route53.describe_zones(ctx)

## Route53 List Records ##
@route53.command(help='Route53 List recoard')
@click.option('--zone-id', type=str, help='update asgname')
@click.pass_context
def describe_records(ctx, zone_id):
    Modules.route53.describe_records(ctx, zone_id)


######################
##   S3 Function   ##
######################

## S3 Bucket List ##
@s3.command(help='S3 List API')
@click.pass_context
def list_buckets(ctx):
    Modules.s3.list_buckets(ctx)


if __name__ == '__main__':
#    main()
    cli()
