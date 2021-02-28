# language: en

Feature: Sum
    Scenario: basic addition
        When sum "2" with "2"
        Then the result should be "4"
