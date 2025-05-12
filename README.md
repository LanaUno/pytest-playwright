## Automated Web Testing with Playwright and Pytest

This project focuses on automating testing of the web application https://www.automationexercise.com/using
Playwright and Pytest. The main goal is to ensure that the functionality, performance, 
and user experience of the website meet the specified requirements. The project is integrated 
with GitHub Actions for automated test runs on every push request.
Test results are published to Allure Report, and  notifications are sent after each 
test run into Slack to get update on the current status.

### Project Structure:
##### * tests/ - Directory containing test cases.
##### * data/ - Directory containing test data.
##### * pages/ - Page Object Model (POM) structure for better maintainability.
##### * conftest.py - Shared fixtures and hooks for setup and teardown.
##### * requirements.txt - List of required packages for the project.

### Steps to set up and run

##### 1. Install Phyton 3.13 version
##### 2. Clone the project https://github.com/LanaUno/pytest-playwright.git
##### 3. Go to the folder cd ./pytest-playwright
##### 4. Add to the root folder file .env with the following content:
```
MY_EMAIL=your own valid random email
MY_PASS=your own valid random password
BASE_URL=https://www.automationexercise.com/
```
##### 5. Project already has all dependencies installed but if necessary

###### install the Pytest plugin:
```
pip install pytest-playwright
```
###### install the required browsers:
```
playwright install
```
###### install allure report:
```
pip install pytest-playwright
```
##### 6. To run test suit use
```
pytest
```
##### 7. To run one particular test
```
pytest ./tests/<test name>
```
##### 8. To generate Allure report run 
```
pytest --alluredir results
```
###### and then 
```
allure serve results
```
##### 8. To run tests in parallel use 
```
pytest -n auto
```
###### With this call, pytest will spawn a number of workers processes equal to the number of available 
###### CPUs, and distribute the tests randomly across them. To run particular quantity of workers 
###### right a number instead of 'auto':
```
pytest -n 5
```
