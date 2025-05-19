# ATTT – Automated Test Suite for GB ATMs and CAS (using SikuliX)

This repository provides a publicly available tests for General Bytes ATMs and CAS.

## Overview

General Bytes (GB) has developed ATTT to help operators efficiently automate testing of their BATM fleet.  
ATTT ensures error-free, stable operation across a wide range of configurations, reducing testing time from days to
hours.

## Use Cases

- Verifying new pre-production BATM software releases
- Automatically checking transaction flows
- Testing negative scenarios and other cases

## Requirements

- **Java Development Kit (JDK) 8** (OpenJDK or Oracle JDK/JRE)
- **SikuliX IDE 2.0.5** ([Download link](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar))

    Officially tested on JDK 8; Java 9+ is supported but may require additional JVM flags
- **64-bit operating system** (Windows, macOS or Linux) — SikuliX supports only 64-bit systems
- **FAT32-formatted USB flash drive**
- **ATTT activation** provided by GB Support

## Security
- Communication with the ATTT server is only possible using unique client certificates issued by GB.
- These certificates must be physically uploaded to each terminal using a FAT32-formatted USB flash drive.
> **Note:** A FAT32-formatted USB flash drive is required to upload certificate to the terminal during activation.
- The ATTT system has been independently security audited.
- 
## Architecture

**Key Components:**

- **ATTT Connector**  
  Streams the terminal’s screen to the ATTT server and processes click events, virtual cash insertions, QR scans, and
  keyboard inputs.

- **ATTT Server**  
  Hosted and maintained by GB; enables remote control of terminals via a web browser.  
  [https://attt.generalbytes.com](https://attt.generalbytes.com)

- **SikuliX**  
  Automation tool that lets QA engineers write Python scripts for visual recognition and interaction on terminal
  screens.

## Setup & Activation

> ⚠️ **Warning:**
> This tool is **not recommended** for use on terminals connected to production CAS servers.
> Proceed **at your own risk**.

### Risks

- Sending real cryptocurrency to wallets without any fiat deposited
- Inadvertent dispensing of cash during automated sell flows
- Locking up the terminal or corrupting its configuration
- Exposing private keys or session tokens if the environment is not properly isolated

### 1. Request Activation

Contact GB Support to request access to the ATTT server by providing your terminal serial numbers and user email
addresses:

- **Support portal:** [Create a Support Ticket](https://generalbytes.atlassian.net/wiki/spaces/ESD/pages/934609035)

### 2. Configure Terminal Details in CAS

**Custom Strings (on the terminal detail page):**

- Add the `attt` flag to the `special_configuration` custom string.

> ⚠️ **Warning:** Without this, ATTT will not work for the terminal!

- Add the following key-value pairs _(case-sensitive: must match exactly)_:
    - `terms_and_conditions`: **TERMS AND CONDITIONS**
    - `scam_disclaimer`: **SCAM DISCLAIMER**
    - `custom_pep_question`: **PEP QUESTION**
    - `required_disclosures_text`: **REQUIRED DISCLOSURES**
    - `privacy_policy`: **PRIVACY POLICY**
    - `marketing_opt_in_agreement_text` : **Marketing agreement text. Agree?**

**Discounts:**

- Discount Type: **Discount from fee**
- Set all discount values (`Discount From Buy Profit Fee`, `Discount From Sell Profit Fee`, `Buy Fixed Fee Discount`,
  `Sell Fixed Fee Discount`) to **100.00%**.
- Select required crypto currencies: **BTC**, **LBTC**, **LTC**, **ETH**.
- Configuration Cash Currency - Set default cash currency to **USD**.
- Set **Valid From** and **Valid To** dates to define the period the discount is active (e.g., `01.09.2024` –
  `01.02.2030`)

**Crypto Settings:**

- For each supported currency (**BTC, LBTC, LTC, ETH**):
- Configuration Currencies - Set default cash currency to **USD**.

**Buy Settings:**

- **Minimum Buy Cash Amount per Transaction:** 100.00
- **Minimum Buy Card Amount per Transaction:** 0.00
- **Buy Rate Source:** Demo Rate Source
- **Hot Wallet Buy:** Demo Wallet
- **Exchange Buy:** Demo Exchange
- **Buy Profit (%):** 10.00%
- **Fixed Transaction Fee:** 10.00

**Sell Settings (except ETH):**

- **Sell Rate Source:** Demo Rate Source
- **Hot Wallet Sell:** Demo Wallet
- **Exchange Sell:** Demo Exchange
- **Sell Strategy - 1:** Receive coins to the Hot Wallet
- **Sell Profit (%):** 10.00%
- **Fixed Transaction Fee:** 10.00

> **Note:** ETH does not support a sell wallet, so sell transactions for ETH are not tested.

**Fiat Settings:**

- **Fiat Currency:** USD - United States dollar
- **Accept All Banknotes**

**AML/KYC Setting:**

- Select the following checkboxes (✓):
    - Reject PEPs
    - Allow withdrawals only for the same identity as sell transaction
    - Verify Wallet Ownership

**KYC and Customer Limits**

- Set **Default Fiat Currency** to **USD - United States dollar**
- For **Registered** and **Unregistered Customers**:
    - Require **Cellphone Number**
- **Anonymous:** Cash Limit Per Transaction = `500.00` (check **Enable cash payments**)
- **Unregistered:** Cash Limit Per Transaction = `1000.00` (check **Enable cash payments**)
- **Registered:** Cash Limit Per Transaction = `5000.00` (check **Enable cash payments**)
- In **Total Terminal Limits**:
    - Cash Limit Per Day For Buy = `100000.00`
    - Cash Limit Per Day For Sell = `100000.00`

**Printing Settings:**

- Select the following checkboxes (✓):
    - Disable Printer Warnings
- Print Buy Receipt — set value to **Never**
- Print Withdrawal Receipt — set value to **Never**
- Sell Tickets Delivery: set to **None** (to be used with withdrawal using phone number)

> **Tip:** Disabling printer warnings and setting receipt printing to “Never” or “None” helps prevent unwanted paper
> slips from being printed or falling out of the terminal.


**Administration Settings:**  
Select the following checkboxes (✓):
- Allow Balance Check
- Disable Door Sensor
- Use Hardcoded Blacklist Addresses
- Don’t Accept Cash If You Don’t Have Enough Supply
- Allow Email or SMS Purchases
- QR Code Sticker Detection
- Hide Redeem Button When Sell Is Not Possible
- Cash Fraud Detection
- Customer Can Cancel Transaction
- Show Marketing Agreement Screen
- Blur Detection Limit: 1
- Withdraw Configuration: Withdraw using QR code or phone number

**Languages:**
- **Default Language:** en - English
- **Preferred Languages:** cs - Czech, de - German, es - Spanish, ar - Arabic, fi - Finnish, ja - Japanese, fr - French,
  bg - Bulgarian, el - Greek, et - Estonian, hi - Hindi, hr - Croatian, hu - Hungarian, hy - Armenian, it - Italian,
  kk - Kazakh, ko - Korean, lv - Latvian, he - Hebrew, ht - Haitian, ka - Georgian, mk - Macedonian, lt - Lithuanian,
  nl - Dutch, no - Norwegian, pl - Polish, pt - Portuguese, ru - Russian, ro - Romanian, sk - Slovak, sl - Slovenian,
  sr - Serbian, sr - Serbian, th - Thai, tr - Turkish, uk - Ukrainian, vi - Vietnamese, sq - Albanian, zh - Chinese.

**Publish Settings:**
- The `Publish` checkbox **must NOT** be selected.

**Terminal Template:**
- You can save all required settings in a Terminal Template and select it in the "Use Terminal Template" field, instead of configuring each setting manually.

> **Note:** Reboot the terminal after configuration (recommended, but not required). 

### 3. Upload Activation Keys (on the BATM terminal)

- Extract the activation ZIP archive (received from GB Support) to a FAT32-formatted USB drive.  
   The file must be named `attt.bks`
- **On the BATM terminal:**  
   Open the **Advanced Administration** menu.
> **Tip:** For more details, refer to the [Knowledge Base](https://generalbytes.atlassian.net/wiki/spaces/ESD/pages/3554541570/ATTT+-+Automated+Testing+Tool+for+Terminal).
- Click on the **UPLOAD ATTT KEYS** button.
- Insert the USB drive into any available USB port on the BATM.
   If all USB ports are in use, you may temporarily disconnect the printer.
   After successful upload, a notification will appear.
- Remove the USB drive (and reconnect the printer if necessary).
- In the Advanced Administration menu, press the button **ENABLE ATTT**.  
   The terminal will now establish a secure connection to the ATTT server.
> ⚠️ The **UPLOAD ATTT KEYS** option will only be visible if the `attt` flag is set in the `special_configuration` custom string for this terminal in CAS.

## Running Tests

- Open the ATTT server at [https://attt.generalbytes.com](https://attt.generalbytes.com).
- Click the **Control terminal** button to access the BATM’s console.
- Clone this repository to your local machine:
   ```bash
   git clone https://github.com/GENERALBYTESCOM/batm_test_public.git
  ```
- Start SikuliX IDE:
    - Open a terminal or command prompt.
    - Navigate to the folder where SikuliX IDE was downloaded (for example, ~/Downloads).
    - Run:
  ```bash
    java -jar sikulixide-2.0.5.jar
  ```
- In SikuliX IDE:
    - Click File → Open
    - Select and open a test file from the cloned `batm_test_public` repository.
    - Click the `Run` button.

## Troubleshooting
- Ensure screen resolution and display scaling are set to 100%.
- Supported screen resolutions:
        1920×1080 (16:9)
        1600×900  (16:9)
        1366×768  (16:9)
        1280×720  (16:9)
        1680×1050 (16:10)
        1440×900  (16:10)
        1280×800  (16:10)   
- Tests are optimized for these screen resolutions. Using unsupported resolutions may cause SikuliX visual matching to fail.
- Tests are designed and verified on BATM 10 terminals. Other models may require adjustments.
