#! /usr/bin/env python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
from tqdm import tqdm
import time

## EC2 List ##
def describe_instances(ctx, instance_id):
    table = PrettyTable(['InstanceName', 'InstanceId', 'InstanceType'])
    table.align['InstanceName','InstanceId','InstanceType'] = 'l'

    response=[]
    instance_ids = [instance_id] if instance_id else []
    response = ctx.parent.params['client'].describe_instances(InstanceIds=instance_ids)
    instance_count = len(response['Reservations'])

    for i in tqdm(range(0, instance_count)):
    #for i in range(0, instance_count):
        table.add_row([
                       response['Reservations'][i]['Instances'][0]['Tags'][0]['Value'],
                       response['Reservations'][i]['Instances'][0]['InstanceId'],
                       response['Reservations'][i]['Instances'][0]['InstanceType'],
                      ])
        time.sleep(0.02)
    print (table)

## start-Instance ##
def start_instances(ctx, instance_id):
    instance_ids = [instance_id]
    try:
        ctx.parent.params['client'].start_instances(InstanceIds=instance_ids)
        print('Start Success')
    except:
        print('Error')

    print('completed')

## stop-instance ##
def stop_instances(ctx, instance_id):
    instance_ids = [instance_id]
    try:
        ctx.parent.params['client'].stop_instances(InstanceIds=instance_ids)
        print('Stop Success')
    except:
        print('Error')

    print('completed')

## AMI List ##
def describe_ami(ctx):
    images=[]
    sorted_ami=[]
    table = PrettyTable(['ImageName','CreateDate'])
    table.align['ImageName','CreateDate'] = 'l'

    try:
        images = ctx.parent.params['client'].describe_images(Owners=["self"])["Images"]
        for ami in sorted(images, key = lambda x:x['CreationDate']):
            sorted_ami.append(ami)

        for i in range(0, len(sorted_ami)):
            table.add_row([sorted_ami[i]['Name'],sorted_ami[i]['CreationDate']])
        print(table)
    except:
        print('Error')

    print('completed')

## Create AMI ##
def create_ami(ctx, instance_id, aminame):
    instance_ids = instance_id
    aminmaes = aminame

    try:
        response = ctx.parent.params['client'].create_image(
            InstanceId = instance_ids,
            Name = aminmaes,
            Description = aminmaes,
            NoReboot = True
        )
    except:
        print('Error')

    print('completed')
