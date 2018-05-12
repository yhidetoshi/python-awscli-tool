#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from prettytable import PrettyTable

def describe_zones(ctx):
    table = PrettyTable(['Domain_Name','Zone_ID'])
    table.align['Domain_Name', 'Zone_ID'] = 'l'
    response=[]
    response = ctx.parent.params['client'].list_hosted_zones()

    try:
        for i in range(0, len(response['HostedZones'])):
            table.add_row([
                response['HostedZones'][i]['Name'],
                response['HostedZones'][i]['Id'],
            ])
    except:
        print('Error')

    print(table)
    print('completed')


def describe_records(ctx, zone_id):
    #table = PrettyTable(['Type','Name','TTL'])
    #table2 = PrettyTable(['Value'])
    #table.align['Type','Name','TTL'] = 'l'
    response=[]
    response = ctx.parent.params['client'].list_resource_record_sets(
            HostedZoneId = zone_id
    )
    #print(response)

    # 暫定の出力表示...
    print("| Type |    Name   |   TTL |   Value   |")
    for i in range(0, len(response['ResourceRecordSets'])):
        print("| "+response['ResourceRecordSets'][i]['Type']+ " | ", end="")
        print(response['ResourceRecordSets'][i]['Name']+ " | ", end="")
        print(str(response['ResourceRecordSets'][i]['TTL'])+ " | ", end="")

        for j in range(0, len(response['ResourceRecordSets'][i]['ResourceRecords'])):
            print(response['ResourceRecordSets'][i]['ResourceRecords'][j]['Value'], end="")
    #        table.add_row([
        print(" |")
    #                     ])
    #print(table)
