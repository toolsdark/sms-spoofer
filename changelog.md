### Changes made in send_sms.py (16/02/2024)

🛠️ **Technical Changes:**
- Utilized the `python-dotenv` library to load the API key from an `api.env` file, enhancing code security and resolving the CVE python/NoHardcodedCredentials.
- Added a check to ensure the presence of the API key in the `api.env` file. In case of absence, an error message is displayed, and the application exits.

🔒 **Security:**
- Resolved CVE python/NoHardcodedCredentials by eliminating direct usage of credentials in the source code.

📦 **Dependencies:**
- Added dependency on the `python-dotenv` library for secure loading of environment variables from files.

🐞 **Bugfix:**
- Addressed a potential security issue related to direct insertion of credentials in the code.

⚙️ **Others:**
- Updated the API key management, improving code security and maintainability.
- Added error notification in case the API key is not present in the `api.env` file.

📝 **Note:**
Ensure to create an `api.env` file in the same directory as the program and insert the API key in the correct format (`SMS_API_KEY=YOUR_API_KEY_HERE`).

### Changes made in README.md (16/02/2024)

🚀 **Features:**
- Added a logo image to enhance visual appeal and branding.
- Included a brief description of the SMS Spoofer Tool and its functionalities.
- Updated the Features section to highlight simplicity, support, attachments, and spoofing capabilities.

📝 **Documentation:**
- Added detailed instructions for installation, including cloning the repository and usage of the program.
- Included a note section to provide additional information on creating the `api.env` file.

🔒 **Security:**
- Added a note section to highlight the importance of securely managing the API key in the `api.env` file.
- Improved security by utilizing the `python-dotenv` library to load the API key securely.

🌐 **Community:**
- Added buttons with links to contact the bot and owner on Telegram for support and inquiries.
- Included badges for stars, pull requests, and issues to encourage community engagement.

🔧 **Miscellaneous:**
- Made minor adjustments to improve readability and organization of content.
