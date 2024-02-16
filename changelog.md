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

