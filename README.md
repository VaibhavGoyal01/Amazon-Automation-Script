# Amazon Automation Script

This project is a Python-based automation script that automates the process of searching for a mobile on Amazon India, applying filters, and adding the first search result to the cart. The script uses the Selenium WebDriver for browser automation and logging for tracking the execution of each step.

## Features

- **Navigate to Amazon India**: The script automatically navigates to the Amazon India homepage.
- **Search for Products**: It searches for the keyword "mobile."
- **Apply Filters**: Applies a 4-star rating filter and sets a price range of ₹10,000 - ₹20,000.
- **Select First Product**: Opens the first product from the search results.
- **Add to Cart**: Adds the selected product to the cart.
- **Screenshots**: Takes screenshots at each step of the process and saves them in the `screenshots` directory.
- **Logging**: Logs each step and any errors encountered during the execution.

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver (Ensure that the `chromedriver` is in your system's PATH)
- Google Chrome browser

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/amazon-automation.git
    cd amazon-automation
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium
    ```

3. Ensure that ChromeDriver is installed and in your PATH:
    - Download ChromeDriver from the official site: https://sites.google.com/a/chromium.org/chromedriver/
    - Add the ChromeDriver executable to your system's PATH.

## Usage

1. Run the script:
    ```sh
    python amazon_automation.py
    ```

2. The script will perform the following actions:
    - Open Amazon India.
    - Search for "mobile."
    - Apply the 4-star filter.
    - Set a price range of ₹10,000 - ₹20,000.
    - Open the first product in the search results.
    - Add the product to the cart.

3. After execution, screenshots of each step will be saved in the `screenshots` directory, and logs will be recorded in the `amazon_automation.log` file.

## Troubleshooting

- **WebDriverException**: Ensure that the version of ChromeDriver matches your installed Chrome browser version.
- **ElementNotVisibleException**: Some elements may take longer to load; increase the wait time in `WebDriverWait`.


## Contributing

Feel free to fork this project, open issues, or submit pull requests if you find any bugs or want to add new features.

## Acknowledgments

- [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- [ChromeDriver Documentation](https://sites.google.com/a/chromium.org/chromedriver/)

