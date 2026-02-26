# 📧 Gmail to Google Sheets Automation

## 🎯 What This Project Does

Ever wished you could automatically log your important emails into a spreadsheet without manual copy-pasting? 

This smart Python automation system reads your unread Gmail messages and magically transforms them into organized rows in Google Sheets. No more tedious data entry - just set it up once and watch it work!

### ✨ Why You'll Love This
- **Set & Forget** - Runs automatically whenever you need it
- **Zero Duplicates** - Smart tracking ensures no email gets logged twice
- **Crystal Clear** - Converts messy HTML emails into clean, readable text
- **Super Safe** - Uses Google's official OAuth (no password sharing!)

## 🏗️ How It Works (The Magic)

```
📧 Gmail (Unread)  →  🐍 Python Script  →  📊 Google Sheets
```

**The Simple Flow:**
1. 🔍 **Finds** your unread emails automatically
2. 📝 **Parses** sender, subject, date & content
3. 📋 **Logs** everything neatly into your spreadsheet
4. ✅ **Marks** emails as read (so they won't appear again)

## 🚀 Get Started in 4 Easy Steps

### What You Need First
- Python 3.7+ installed
- A Google account (with Gmail & Sheets access)

### Step 1: Grab the Code
```bash
git clone https://github.com/shubhamdagar9854/gmail-to-google-sheets-final
cd gmail-to-sheets
```

### Step 2: Install the Goodies
```bash
pip install -r requirements.txt
```

### Step 3: Connect Your Google Account
- Head over to [Google Cloud Console](https://console.cloud.google.com/)
- Create a new project (or pick an existing one)
- Turn on **Gmail API** and **Google Sheets API**
- Create **OAuth 2.0 credentials** (Desktop Application type)
- Download your `credentials.json` file

### Step 4: Set Up & Run
```bash
mkdir -p credentials
# Place your credentials.json in the credentials/ folder
python src/main.py
```

**First time?** Your browser will pop up asking for permission - just click "Allow" and you're all set!

## 🔐 Security First!

**Your data is safe because:**
- ✅ **No passwords stored** anywhere in the code
- ✅ **Official Google OAuth** authentication
- ✅ **Tokens saved locally** on your machine only
- ✅ **Read-only access** to emails you choose to process

## 📊 What Gets Logged in Your Sheet

| Column | What It Contains | Example |
|--------|------------------|---------|
| **From** | Sender's email | `john@company.com` |
| **Subject** | Email subject line | `Meeting Tomorrow at 3PM` |
| **Date** | When it was sent | `Mon, 26 Feb 2026 20:44:00` |
| **Content** | Email body (plain text) | `Hey, let's discuss the project...` |

## 🛡️ Smart Features That Make Life Easy

### 🎯 **Duplicate Prevention**
- Each email gets a unique ID that we remember
- Already processed? We'll skip it automatically
- Run the script 100 times - still no duplicates!

### 🔄 **Error Recovery**
- Internet hiccup? No problem - we'll handle it gracefully
- Weird email format? We'll still try to extract what we can
- Something goes wrong? You'll see exactly what happened

### 📏 **Content Smartness**
- Super long emails? We'll trim them to fit in Google Sheets
- HTML emails? Automatically converted to clean text
- Special characters? Handled with care

## 🎮 Running the Show

### Quick Start
```bash
python src/main.py
```

### What You'll See
```
🚀 Starting Gmail to Sheets sync...
✅ Connected to Gmail and Google Sheets
📧 Found 5 unread messages
✅ Processed: Project Update - Q1 Results...
✅ Processed: Meeting Reminder - Tomorrow 3PM...
🎉 Sync complete!
📊 Processed: 5 emails
⏭️  Skipped: 0 duplicates
```

## 🧪 Want to Test It?

```bash
python test_email_parser.py
```

## 📝 Real-World Benefits

- **⏰ Save Hours** - No more manual email logging
- **📈 Stay Organized** - All your important emails in one place
- **🔄 Never Miss Anything** - Automatic logging means nothing falls through cracks
- **📊 Easy Analysis** - Sort, filter, and analyze your emails in Sheets

## � Things to Know

- Only processes **unread inbox emails** (sent items, drafts, etc. are ignored)
- **Attachments** aren't included (just the text content)
- Very long emails get **trimmed** to fit in spreadsheet cells
- Processes emails **one by one** (not in batches - more reliable!)

## 🔮 What's Next? (Future Ideas)

- [ ] 📎 Handle email attachments
- [ ] 🎯 Custom filtering rules
- [ ] 📊 Multiple spreadsheet support
- [ ] 🌐 Web dashboard interface
- [ ] ⏰ Scheduled automatic runs

## 🎪 Proof It Works!

Check out the `/proof` folder for screenshots showing:
- 📧 Gmail inbox with unread emails
- 📊 Google Sheet populated with data
- 🔐 OAuth consent screen in action

## 🤝 Contributing

Found a bug or have an idea? I'd love to hear from you!

## 📄 License

Built with ❤️ for the Incubation Program

---

## 👋 About the Developer

Hi! I'm **Shubham Dagar**, a passionate developer who loves building practical automation tools that solve real-world problems. This project was created as part of a technical assignment to demonstrate clean coding practices and problem-solving skills.

**🚀 Let's connect!**
- **GitHub:** https://github.com/shubhamdagar9854
- **Email:** shubhamdagar9854@gmail.com

---

*This project isn't just code - it's a solution that saves time and reduces tedious work. Because the best automation is the kind that just works, quietly in the background.* 🎯