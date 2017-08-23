import thriftpy
import time
from thriftpy.rpc import make_client
from behave import *
from features.generic.constant import constant


@given('we need to load "{filename}" thrift file in memory')
def step_impl(context, filename):
    file = str(filename)
    context.timeline= thriftpy.load(constant.timlineThriftPath,module_name=file + "_thrift")

@given('make client with "{serviceName}" service')
def step_impl(context, serviceName):
    service = str(serviceName)
    if service == 'LifecycleReportingService':
        context.client = make_client(context.timeline.LifecycleReportingService, '127.0.0.1', 8099)
    else:
        print('No Such Service to make connection to Client')


@then('make call to getCampaignExecutionDetails for orgId "{orgId}" and orgConfigId "{orgConfigId}"')
def step_impl(context,orgId,orgConfigId):
    context.LifecycleStatsObject = context.client.getCampaignExecutionDetails(context.timeline.SessionId(**constant.session(int(orgId),int(orgConfigId))), int(time.time()))

@then('validate the results for campaign')
def step_impl(context):
    listTimelineStats=context.LifecycleStatsObject.timelineStatistics
    for lenlistTimelineStats in listTimelineStats:
        lenlistTimelineStats.timeline              ## Returns a Object Timeline
        lenlistTimelineStats.messageStats          ## Returns a Object UserExecutionStats
        lenlistTimelineStats.milestoneStatistics   ## Returns a List of MilestoneStats
        lenlistTimelineStats.statusCount           ## Returns a map<ExecutionStatus, i32>
        print("Discuss how to get meaningfull data")