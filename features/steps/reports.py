import thriftpy
import time
from thriftpy.rpc import make_client
from behave import *
from features.generic.constant import constant


@given('we need to load "{filename}" thrift file in memory')
def step_impl(context, filename):
    ##Code to put here

@given('make client with "{serviceName}" service')
def step_impl(context, serviceName):
    ##Code to put here

@then('make call to getCampaignExecutionDetails for orgId "{orgId}" and orgConfigId "{orgConfigId}"')
def step_impl(context,orgId,orgConfigId):
    ##Code to put here
    
@then('validate the results for campaign')
def step_impl(context):
    ##Code to put here
