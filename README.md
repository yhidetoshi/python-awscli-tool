## README

![Alt Text](https://github.com/yhidetoshi/Pictures/raw/master/aws/aws-python.png)

勉強しながら作成中...

### EC2
```
■ Instance一覧
  > $ python ec2.py ec2 describe_instances

■ Instance起動
  > $ python ec2.py ec2 run_instances --instance-id=i-xxxxxxxxxxx

■ Instance停止
  > $ python ec2.py ec2 stop_instances --instance-id=i-xxxxxxxxxxx

■ AMI一覧(作成順にソート)
  > $ python ec2.py ec2 describe_ami
```
