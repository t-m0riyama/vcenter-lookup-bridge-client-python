#!/bin/bash


echo "==== Clear Test Results"
#(cd /allure-results && /bin/rm -f *.json)
(cd ./allure-results && /bin/rm -f *.json)

echo "==== Execute Test Suites"
# (cd / && pytest -vv --tb=short -s -n 1 --alluredir=/allure-results tests)
# (cd / && pytest -vv --tb=short -n 4 -p allure_pytest_bdd --gherkin-terminal-reporter tests)
#(cd / && pytest tests)
(pytest tests)

echo "==== Send Test Results to Allure"
(scripts/send_test_results.sh)
