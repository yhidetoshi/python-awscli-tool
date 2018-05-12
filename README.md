## README

![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/aws/aws-python.png)

作成中...

- Pythonについて
  - Python 3.6.5(virtualenvを利用)
  
- 使い方
  - `$ git clone https://github.com/yhidetoshi/python-awscli-tool`
  - `$ cd python-awscli-tool`
  - `$ pip install sys prettytable click boto3 json tqdm time`
  - awscli.pyをコマンドオプションをつけて実行する

### EC2
```
■ Instance一覧
  > $ ./awscli.py ec2 describe_instances
    ■ profileの場合
    > $ ./awscli.py -p <PROFILENAME> ec2 describe_instances
  
■ Instance起動
  > $ ./awscli.py ec2 run_instances --instance-id=i-xxxxxxxxxxx

■ Instance停止
  > $ ./awscli.py ec2 stop_instances --instance-id=i-xxxxxxxxxxx

■ Instance削除
  > $ ./awscli.py ec2 terminate_instances --instance-id=i-xxxxxxxxxxx

■ AMI一覧(作成順にソート)
  > $ ./awscli.py ec2 describe_ami

■ AMI作成(Register)
  > $ ./awscli.py ec2 create_ami --imageid=ami-xxxxxxx

■ AMI削除(Deregister)
  > $ ./awscli.py ec2 delete_ami --imageid=ami-xxxxxxx
```

### AutoScaling
```
■ AutoScaling情報一覧
  > $ ./awscli.py asg describe_asg

■ AutoScaling Maxの変更
  > $ ./awscli.py asg update_max --asgname=ASGNAME --max=NUM

■ AutoScaling Minの変更
  > $ ./awscli.py asg update_min --asgname=ASGNAME --min=NUM

■ AutoScaling Desireの変更
  > $ ./awscli.py asg update_desire --asgname=ASGNAME --desire=NUM
```

### Route53
```
■ Zone一覧
  > $ ./awscli.py route53 describe_zones
■ Zoneid指定のレコード情報取得
  > $ ./awscli.py route53 describe_records --zone-id=ID
```

### S3
```
■ バケット一覧
  > $ ./awscli.py s3 list_buckets 
```
