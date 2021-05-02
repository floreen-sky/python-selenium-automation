# Created by Flo at 5/1/2021

Feature: Amazon - Actions

# Home Work 9.1

  Scenario Outline: Search for an Item in a different Amazon Department using Dropdown
    Given Open Amazon Page
    When Select <department> Department
    Then Input <search_item> in the search Box and click search
    Then Verify if <department> Department is selected
    Examples:
    |department   |search_item  |
    |handmade     |painting     |


# Home Work 9.2

  Scenario Outline: Verify Deals in New Arrivals
    Given Open Amazon product B074TBCSC8 page
    When Hover over New Arrival button
    Then Verify if <deal> Deal is visible
    Examples:
    |deal   |
    |Women  |
    |Men    |
