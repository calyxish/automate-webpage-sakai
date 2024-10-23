# Automated Sakai Login Script Using Selenium and Python
## 1. Description
### Situation:
Manually logging into the Sakai e-learning platform every time I needed access felt repetitive and time-consuming. Each session required opening the browser, navigating to the login page, and entering my credentials, which detracted from my efficiency.

### Task:
I wanted to streamline this process by automating the login procedure. My goal was to create a script that would automatically open my preferred browser, enter my credentials securely, log me into Sakai, and keep the browser open for a duration I could control. This would save me time and allow me to focus on my tasks rather than dealing with repeated manual logins.

### Action:
To achieve this, I used Python and Selenium to develop a script that automates the entire login process. The script securely takes in user credentials, navigates to the Sakai platform's login page, and automatically submits the login form. I also built in a timer that allows the browser to stay open for a user-specified period before automatically closing. The script is designed to be run on demand, giving me full control over when I access the platform.

### Result:
The automated login script has significantly improved my workflow, eliminating the need to manually log in every time. Now, I can log in to Sakai with a single command, which saves time and reduces the repetitive tasks in my daily routine. Additionally, it provides a practical demonstration of browser automation with Selenium, which can be applied to other similar tasks in the future.

## 2. Table of Contents

- [Project Preview](#3-project-preview)
- [Installation](#4-installation)
- [Dependencies](#5-dependencies)
- [Usage](#6-usage)
- [Contributing](#7-contributing)
- [License](#8-license)
- [Contact Information](#9-contact-information)
- [Acknowledgements](#10-acknowledgements)

## 3. Project Preview

![Project Preview]()


## 4. Installation

1. Clone the repository:
   ```sh markdown
   HTTPS
   git clone https://github.com/calyxish/automate-webpage-sakai.git

   GitHub CLI
   git gh repo clone calyxish/automate-webpage-sakai

   ```
2. Navigate to the project directory
   ```sh
   cd automate-webpage-sakai
   ```
3. Install required packages
   ```sh markdown
    pip install -r requirements.txt
   ```

## 5. Dependencies
   ```sh markdown
   Python 3.x
   Selenium
   requests
   Chrome WebDriver (or any other browser driver)

   ```

## 6. Usage
### Install Chrome WebDriver:
Ensure you have Chrome WebDriver installed and added to your PATH or the appropriate browser driver for your preferred browser.
   ```sh markdown
   webdriver.Chrome()
   ```
### Run the Script:
Enter your credentials when prompted.
The script will automatically log in to Sakai and keep the browser open for 10 seconds (configurable).
   ```sh markdown
    python automate_webpage_sakai.py
   ```


### Important Notes:
Treat your token like a password. Do not share it or expose it in your code (e.g., don't include it directly in your scripts or commit it to your repository).
If you believe your token has been compromised, you can revoke it and generate a new one.

## 7. Contributing

Guidelines for contributing to your project.

```sh markdown

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**. Thank You!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
```

## 8. License

Distributed under ... Not Yet

## 9. Contact Information
Calyx Ish
GitHub: @calyxish

## 10. Acknowledgements

```sh markdown
Selenium for enabling browser automation.

```