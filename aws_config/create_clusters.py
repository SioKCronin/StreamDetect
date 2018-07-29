import boto3, os

# network settings
vpc_cidr = "10.0.0.0/26"
subnet_cidr = "10.0.0.0/28"

# node settings
kafka_instances=5
storm_instances=7

# initialization files
path = "host_install_scripts"
kafka_initfile = os.path.join(path, "kafka_install.sh")
sotrm_initfile = os.path.join(path, "storm_install.sh")

# base AWS settings
base_aws_image = ami-833e60fb

# services
services = ['kafka', 'storm']
