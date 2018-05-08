#! /usr/bin/env python
# -*- coding: utf-8 -*-

def list_buckets(ctx):
    bucketList=[]
    for bucket in ctx.parent.params['client'].buckets.all():
        bucketList.append(bucket.name)
        print(bucket.name)
