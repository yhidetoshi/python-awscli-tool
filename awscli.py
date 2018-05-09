#! /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import boto3
import json

# importモジュール(./Modules/に関数を実装)
import Modules.def_ec2
import Modules.def_s3

@click.group(help='Subcommand click CLI')
@click.option('-p', '--profile', type=str)
@click.pass_context
def main(ctx, profile):
    ctx.params['session'] = boto3.session.Session(profile_name=ctx.params.get('profile'))

## EC2 ##
@main.group(help='EC2 API')
@click.pass_context
def ec2(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('ec2')

## S3 ##
@main.group(help='S3 API')
@click.pass_context
def s3(ctx):
    ctx.params['client'] = ctx.parent.params['session'].resource('s3')

######################
##   EC2 Function   ##
######################

## EC2 List ##
@ec2.command(help='EC2 DescribeInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def describe_instances(ctx, instance_id):
    Modules.def_ec2.describe_instances(ctx, instance_id)

## EC2 start ##
@ec2.command(help='EC2 RunInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def start_instances(ctx, instance_id):
    Modules.def_ec2.start_instances(ctx, instance_id)

## EC2 stop ##
@ec2.command(help='EC2 StopInstances API')
@click.option('--instance-id', type=str, help='specify instance id')
@click.pass_context
def stop_instances(ctx, instance_id):
    Modules.def_ec2.stop_instances(ctx, instance_id)

## AMI List ##
@ec2.command(help='Amazon Linux Image List API')
@click.pass_context
def describe_ami(ctx):
    Modules.def_ec2.describe_ami(ctx)

## AMI CreateAMI
@ec2.command(help='Amazon Linux Image List API')
@click.option('--instance-id', type=str, help='input instanceid')
@click.option('--aminame', type=str, help='input aminame')
@click.pass_context
def create_ami(ctx, instance_id, aminame):
    Modules.def_ec2.create_ami(ctx, instance_id, aminame)

## AMI DeleteAMI
@ec2.command(help='Amazon Linux Image List API')
@click.option('--imageid', type=str, help='input imageid')
@click.pass_context
def delete_ami(ctx, imageid):
    Modules.def_ec2.delete_ami(ctx, imageid)


######################
##   S3 Function   ##
######################

## S3 Bucket List ##
@s3.command(help='S3 List API')
@click.pass_context
def list_buckets(ctx):
    Modules.def_s3.list_buckets(ctx)

if __name__ == '__main__':
    main()
