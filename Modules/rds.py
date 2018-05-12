#! /usr/bin/env python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable

## start-Instance ##
def describe_instances(ctx):
    table = PrettyTable(['DBInstanceIdentifier', 'DBInstanceClass', 'Engine', 'MultiAZ'])
    table.align['DBInstanceIdentifier', 'DBInstanceClass', 'Engine', 'MultiAZ'] = 'l'

    try:
        resopnse=[]
        resopnse=ctx.parent.params['client'].describe_db_instances()
        #print(resopnse)

        for i in range(0, len(resopnse['DBInstances'])):
            table.add_row([
                resopnse['DBInstances'][i]['DBInstanceIdentifier'],
                resopnse['DBInstances'][i]['DBInstanceClass'],
                resopnse['DBInstances'][i]['Engine'],
                resopnse['DBInstances'][i]['MultiAZ'],
            ])
        print(table)

    except:
        print('Error')

    print('End')

## start-Instance ##
def start_instances(ctx, name):
    try:
        ctx.parent.params['client'].start_db_instance(DBInstanceIdentifier=name)
        print('Start Success')
    except:
        print('Error')

    print('End')


## stop-Instance ##
def stop_instances(ctx, name):
    try:
        ctx.parent.params['client'].stop_db_instance(DBInstanceIdentifier=name)
        print('Stop Success')
    except:
        print('Error')

    print('End')
