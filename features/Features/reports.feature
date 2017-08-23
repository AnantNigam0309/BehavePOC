@Timeline_Report
Feature: This Feature Test for Reporting in Timeline Campaign

  @Timeline_Report_Demo
  Scenario: Making a Connection and Executing one Demo Case
    Given we need to load "temporal_engine" thrift file in memory
    And make client with "LifecycleReportingService" service
    Then make call to getCampaignExecutionDetails for orgId "1193" and orgConfigId "1199"
    Then validate the results for campaign