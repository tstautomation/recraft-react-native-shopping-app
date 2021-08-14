@regression @login
Feature: Login Module

  @author_name @test_case_id @smoke
  Scenario: Verify user is able to login
    Given User has launched the application
    When User does login with tst1.automation@gmail.com and Test0001!!
    Then Verify user on homescreen after login