1️⃣ Project Overview

        This project is a Python automation system that reads real unread emails from my Gmail inbox and logs them into a Google Sheet automatically.

        The system connects to:

        Gmail API → to read unread emails

        Google Sheets API → to store email data in rows

        Each processed email is added as one new row in Google Sheets with:

        Sender email

        Subject

        Date & time

        Email body (plain text)

        The script is safe to re-run and does not create duplicate entries.

2️⃣ Architecture Diagram
        High-Level Flow
        +-----------+        +-------------+        +------------------+
        |   Gmail   | -----> |   Python    | -----> |  Google Sheets   |
        |  (Unread) |        |   Script    |        |   (Rows added)   |
        +-----------+        +-------------+        +------------------+


        Explanation:

        Gmail API fetches unread emails

        Python parses email details

        Google Sheets API appends data as rows


3️⃣ Setup Instructions

        Python 3 installed

        Google account (Gmail + Sheets)

        🔹 Step 1: Clone Repository
        git clone <your-repo-url>
        cd gmail-to-sheets

        🔹 Step 2: Install Dependencies
        pip install -r requirements.txt

        🔹 Step 3: Add Credentials

        Create OAuth credentials from Google Cloud Console

        Download credentials.json

        Place it here:

        credentials/credentials.json


        ⚠️ Do NOT commit this file

        🔹 Step 4: Run Script
        python src/main.py


        On first run, a browser window opens for Google login and consent.

4️⃣ OAuth Flow Explanation

        This project uses OAuth 2.0 Desktop Application flow.

        Steps:

        User runs the script

        Google OAuth consent screen appears

        User allows Gmail & Sheets access

        Access token is generated

        Token is stored locally for reuse

        ✔ No service accounts
        ✔ No hard-coded secrets
        ✔ Safe and Google-recommended flow

5️⃣ Duplicate Prevention Logic

        Duplicate emails are prevented using a state file.
        How it works:
        Each Gmail email has a unique message ID
        After processing an email, its ID is saved in state.json

        On next run:
        Script checks if ID already exists
        If yes → email is skipped

        Why this approach?
        Lightweight

        No database required
        Reliable across script re-runs

6️⃣ Challenges Faced & Solutions
        🔹 1. Unicode / Encoding Errors

        Problem:
        Some email bodies contained non-ASCII characters causing Base64 decode errors.

        Solution:
        Used safe decoding with error handling and ignored invalid characters.

        🔹 2. Google Sheets 50,000 Character Limit

        Problem:
        Large emails exceeded single-cell character limit.

        Solution:
        Email content is truncated safely before inserting into Sheets.

        🔹 3. OAuth Test User Access Issue

        Problem:
        Google blocked access because app was in testing mode.

        Solution:
        Added my Gmail account as Test User in Google Auth Platform.

7️⃣ Limitations of the Solution

        Very large emails are truncated
        Only Unread Inbox emails are processed
        Emails are processed sequentially (not batch)
        Attachments are not included

8️⃣ Proof of Execution

        Screenshots included in /proof folder:
        Gmail inbox with unread emails
        Google Sheet populated with rows
        OAuth consent screen
        A 2–3 minute demo video is also provided explaining:
        Project flow
        Duplicate prevention
        Script re-run behavior

✅ Conclusion

        This project demonstrates:
        Real Gmail API integration
        Google Sheets automation
        OAuth 2.0 authentication
        Clean Python code structure
        Safe duplicate handling
        Enhanced error handling and user feedback
        Progress tracking with emoji indicators
        Robust email parsing with fallback handling
        It is a practical real-world automation project.

🚀 Enhanced Features:
- Real-time progress tracking with emoji indicators
- Comprehensive error handling for production use
- Fallback email parsing for malformed messages
- Detailed sync statistics (processed vs skipped)
- User-friendly console output
- Graceful error recovery