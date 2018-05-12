#! /usr/bin/env python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable

## AutoScaling (Describe) ##
def describe_asg(ctx):
    table = PrettyTable(['ASG_Name','Running_Num', 'MinSize', 'MaxSize', 'DesiredCapacity'])
    table.align['ASG_Name', 'Running_Num', 'MinSize', 'MaxSize', 'DesiredCapacity'] = 'l'

    response=[]
    response = ctx.parent.params['client'].describe_auto_scaling_groups()
    try:
        for i in range(0, len(response['AutoScalingGroups'])):
            table.add_row([
                response['AutoScalingGroups'][i]['AutoScalingGroupName'],
                len(response['AutoScalingGroups'][i]['Instances']),
                response['AutoScalingGroups'][i]['MinSize'],
                response['AutoScalingGroups'][i]['MaxSize'],
                response['AutoScalingGroups'][i]['DesiredCapacity'],
             ])
    except:
        print('Error')

    print(table)
    print('completed')

## AutoScaling(Update Max) ##
def update_max(ctx, asgname, max):
    try:
        ctx.parent.params['client'].update_auto_scaling_group(
            AutoScalingGroupName = asgname,
            MaxSize = max
        )
    except:
        print('Error')

    print('completed')

## AutoScaling(Update Min) ##
def update_min(ctx, asgname, min):
    try:
        ctx.parent.params['client'].update_auto_scaling_group(
            AutoScalingGroupName = asgname,
            MinSize = min
        )
    except:
        print('Error')

    print('completed')

## AutoScaling(Update Desire) ##
def update_desire(ctx, asgname, desire):
    try:
        ctx.parent.params['client'].update_auto_scaling_group(
            AutoScalingGroupName = asgname,
            DesiredCapacity = desire
        )
    except:
        print('Error')

    print('completed')
