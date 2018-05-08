#! /usr/bin/env python
# -*- coding: utf-8 -*-

import click
import boto3
import json

# importモジュール
import Modules.def_ec2
import Modules.def_s3

@click.group(help='Subcommand click CLI')
@click.option('-p', '--profile', type=str)
@click.pass_context
def main(ctx, profile):
    ctx.params['session'] = boto3.session.Session(profile_name=ctx.params.get('profile'))

@main.group(help='EC2 API')
@click.pass_context
def ec2(ctx):
    ctx.params['client'] = ctx.parent.params['session'].client('ec2')

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
