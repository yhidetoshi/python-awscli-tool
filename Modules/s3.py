#! /usr/bin/env python
# -*- coding: utf-8 -*-

from prettytable import PrettyTable

def list_buckets(ctx):
    bucketList=[]
    table = PrettyTable(['BucketName'])
    table.align['BucketName'] = 'l'

    try:
        for bucket in ctx.parent.params['client'].buckets.all():
            table.add_row([bucket.name])
            #bucketList.append(bucket.name)
            #print(bucket.name)
    except:
        print('Error')

    print(table)
    print('completed')
