## README

![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/aws/aws-python.png)

- [Pythonについて]
  - Python 3.6.5 と boto3(1.7.11)実装
  - Python 3x系だと動くと思います
  
- [準備]
  - python 3系をインストール
  - `$ git clone https://github.com/yhidetoshi/python-awscli-tool`
  - `$ cd python-awscli-tool`
  - `$ pip install sys prettytable click boto3 json tqdm time`
  - awscli.pyをコマンドオプションをつけて実行する(実行オプションは以下に記載)

- [参考]
  - boto3
    - https://boto3.readthedocs.io/en/latest/
  - click
    - http://click.pocoo.org/5/api/
  - aws-sdk-goで独自実装した版はこちら
    - https://github.com/yhidetoshi/go-awscli-tool
 
- **`$ ./awscli.py --help`**
```
Usage: awscli.py [OPTIONS] COMMAND [ARGS]...

  Subcommand click CLI

Options:
  -p, --profile TEXT
  --help              Show this message and exit.

Commands:
  asg      AutoScaling API
  ec2      EC2 API
  rds      RDS API
  route53  Route53 API
  s3       S3 API
```

- **`$ ./awscli.py ec2 --help`**
```
Usage: awscli.py ec2 [OPTIONS] COMMAND [ARGS]...

  EC2 API

Options:
  --help  Show this message and exit.

Commands:
  create_ami           Amazon Linux Image Create API
  delete_ami           Amazon Linux Image Delete API
  describe_ami         Amazon Linux Image List API
  describe_instances   EC2 DescribeInstances API
  start_instances      EC2 RunInstances API
  stop_instances       EC2 StopInstances API
  terminate_instances  EC2 TerminateInstances API
```

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

### RDS
```
■ インスタンス一覧
  > $ ./awscli.py rds describe_instances

■ インスタンス起動
  > $ ./awscli.py rds start_instances --name={DBInstanceIdentifier}

■ インスタンス停止
  > $ ./awscli.py rds stop_instances --name={DBInstanceIdentifier} 
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
