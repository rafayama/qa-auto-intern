Feature: Tests for Reely search functionality

  Scenario: User can see videos in User guide page
    Given Open Reely main page
    When Logged in
    And Click on Settings button
    And Click on User Guide button
    Then Verify that the right page opens
    And Verify that all lesson videos contain titles