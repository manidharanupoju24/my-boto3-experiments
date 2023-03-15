import boto3
import schedule

# documentation reference :
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html


ec2_client = boto3.client('ec2', region_name="us-west-2")
ec2_resource = boto3.resource('ec2', region_name="us-west-2")


def check_instance_status():
    response = ec2_client.describe_instances()  # gives the list of reservations
    for reservation in response['Reservations']:
        # print(reservation['Instances'])
        for instance in reservation['Instances']:
            instance_id = (instance['InstanceId'])
            instance_state = (instance['State']['Name'])
            print(f"Instance with id {instance_id} is in status : {instance_state}")

    statuses = ec2_client.describe_instance_status()  # gives a list of instance statuses
    for instance_status in statuses['InstanceStatuses']:
        ins_status = instance_status['InstanceStatus']['Status']
        sys_status = instance_status['SystemStatus']['Status']
        print(f"Instance with id {instance_status['InstanceId']} status is {ins_status} and status check is {sys_status}")


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()