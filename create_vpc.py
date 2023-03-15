import boto3

# ec2_client = boto3.client('ec2') # can add a region name along with ec2
ec2_client = boto3.client('ec2', region_name='us-west-2')
ec2_resource = boto3.resource('ec2')


new_vpc = ec2_resource.create_vpc(
    CidrBlock="10.0.0.0/16"
)

new_vpc.create_subnet(
    CidrBlock="10.0.0.0/24"
)

all_available_vpcs = ec2_client.describe_vpcs()

vpcs = all_available_vpcs['Vpcs']

for vpc in vpcs :
    # print(vpc['VpcId'])
    # print(vpc['CidrBlockAssociationSet'])
    cidr_block_association_sets = vpc['CidrBlockAssociationSet']
    for assoc_set in cidr_block_association_sets :
        print(assoc_set['CidrBlockState'])


