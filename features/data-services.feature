Feature: Install and remove data-service

  Scenario: Detect dcos cluster
    Given we have dcos installed
    When can execute dcos cluster list without issue
    Then behave will test them for us!

  Scenario: install kafka service
    Given we have dcos installed
    When install the kafka package
    When create a new topic topic1
    Then behave will test kafka for us!
