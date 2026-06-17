<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=200&section=header&text=RPA%20Challenge%20Bot&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Selenium%20%7C%20Python%20%7C%20Web%20Automation&descAlignY=56&descColor=ffffff" width="100%"/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Chrome](https://img.shields.io/badge/Chrome%20Driver-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://chromedriver.chromium.org)

</div>

---

## 📌 Project Overview

**RPA Challenge Bot** is a Python-based Robotic Process Automation (RPA) solution that autonomously completes the [rpachallenge.com](https://rpachallenge.com) form-filling challenge using **Selenium WebDriver**.

The bot visits the challenge website, downloads the Excel data file, reads 10 employee records, and automatically fills and submits a dynamically rearranging web form — all without any human interaction.

> 🏆 The challenge tests automation accuracy by **randomly shuffling form field positions** on every submission, making it impossible to rely on fixed field order.

---

## ✨ Features

- 🌐 **Automated browser navigation** — Opens Chrome and navigates to rpachallenge.com
- 📥 **Dynamic file download** — Downloads the latest `challenge.xlsx` directly from the site
- 📊 **Excel data parsing** — Reads 10 employee records using Pandas
- 🤖 **Smart form filling** — Locates fields by Angular `ng-reflect-name` attributes, immune to position shuffling
- ✅ **Auto submit** — Clicks submit after each record automatically
- 🔁 **Full loop automation** — Processes all 10 records end-to-end without human input
- 🧹 **Clean re-runs** — Deletes old downloads before fetching a fresh file

---

## 📁 Project Structure

```
rpachallenge-master/
├── 📄 main.py                  # Main automation script (RPACHALLENGE class)
└── 📂 downloads/
    └── 📋 challenge.xlsx       # Excel data file (auto-downloaded at runtime)
```

---

## 🧠 How It Works

```
Open Chrome → Navigate to rpachallenge.com
        ↓
Download challenge.xlsx from the website
        ↓
Parse Excel → Extract 10 employee records
        ↓
Click "Start" to begin the challenge
        ↓
┌─────────────────────────────────┐
│  For each of 10 records:        │
│  → Locate form fields by name   │
│  → Fill all 7 fields with data  │
│  → Click Submit                 │
└─────────────────────────────────┘
        ↓
Challenge Complete ✅
```

---

## 📋 Data Fields Automated

The bot reads and fills the following 7 fields for each of the 10 records:

| Field | Excel Column | Example |
|---|---|---|
| First Name | `First Name` | John |
| Last Name | `Last Name` | Smith |
| Company Name | `Company Name` | IT Solutions |
| Role in Company | `Role in Company` | Analyst |
| Address | `Address` | 98 North Road |
| Email | `Email` | jsmith@itsolutions.co.uk |
| Phone Number | `Phone Number` | 40716543298 |

---

## 🏗️ Class Architecture

```
RPACHALLENGE
│
├── __init__()        Sets up ChromeDriver, navigates to site, inits data lists
├── download_file()   Removes old file, downloads fresh challenge.xlsx
├── handle_xlsx()     Reads Excel with Pandas, loads data into lists
├── start()           Clicks the Start button on the website
├── enter_data()      Loops through 10 records, calls input_data + submit_data
├── input_data(id)    Fills all 7 form fields for a given record index
├── submit_data()     Clicks the Submit button
└── close()           Quits the browser
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

### Installation

```bash
# Clone the repository
git clone https://github.com/Hirushan-Liyanage/rpachallenge.git
cd rpachallenge

# Install dependencies
pip install selenium pandas openpyxl
```

### Configuration

Before running, update the download directory path in `main.py` to match your system:

```python
# In __init__(), update this line:
options.add_experimental_option("prefs", {
    "download.default_directory": "C:\\Users\\YourUsername\\path\\to\\rpachallenge\\downloads"
})
```

> On **Mac/Linux**, use a forward-slash path:
> ```python
> "download.default_directory": "/home/youruser/rpachallenge/downloads"
> ```

### Run

```bash
python main.py
```

The browser will open automatically, complete the challenge, and display the final score on screen.

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| **Python 3** | Core scripting language |
| **Selenium WebDriver** | Browser automation & DOM interaction |
| **Pandas** | Excel file reading and data extraction |
| **openpyxl** | Excel `.xlsx` file engine for Pandas |
| **ChromeDriver** | Chrome browser automation driver |

---

## ⚙️ Why `ng-reflect-name` Selectors?

The RPA Challenge is designed to **shuffle form field positions** after every submission — making positional selectors (like XPath index or CSS order) unreliable. This bot targets fields using Angular's `ng-reflect-name` attribute, which stays constant regardless of where the field appears on screen:

```python
# Example — finds First Name field no matter where it is on the page
driver.find_element(By.CSS_SELECTOR, 'input[ng-reflect-name="labelFirstName"]')
```

This is the correct RPA approach — locate by **semantic identity**, not visual position.

---

## 📦 Dependencies

```txt
selenium
pandas
openpyxl
```

Install all at once:

```bash
pip install selenium pandas openpyxl
```

---

## 🔮 Possible Improvements

- [ ] Add `requirements.txt` for easy dependency installation
- [ ] Replace hardcoded download path with a dynamic `os.getcwd()` path
- [ ] Add headless mode support for running without a visible browser window
- [ ] Improve timing with `WebDriverWait` instead of `time.sleep()`
- [ ] Add logging for each submitted record
- [ ] Capture and save the final score screenshot

---

## 👨‍💻 Author

**Hirushan Liyanage**
> BSc (Hons) Information Technology — Data Science | SLIIT

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/Hirushan-Liyanage)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:kaveeshaliyanage08@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Hirushan-Liyanage)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12&height=100&section=footer" width="100%"/>
</div>
