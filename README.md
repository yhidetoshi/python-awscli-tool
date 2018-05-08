## README

![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/aws/aws-..png)

勉強しながら作成中...

### EC2
```
■ Instance一覧
  > $ ./awscli.py ec2 describe_instances

■ Instance起動
  > $ ./awscli.py ec2 run_instances --instance-id=i-xxxxxxxxxxx

■ Instance停止
  > $ ./awscli.py ec2 stop_instances --instance-id=i-xxxxxxxxxxx

■ AMI一覧(作成順にソート)
  > $ ./awscli.py ec2 describe_ami
```
