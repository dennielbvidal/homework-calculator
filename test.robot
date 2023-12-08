*** Settings ***
Library  SeleniumLibrary
Library  Process

*** Keywords ***
Compute
    ${result}  Run Process    python    calculator.py
      BuiltIn.Log To Console  ${result}

*** Test Cases ***
Calculator
    Compute