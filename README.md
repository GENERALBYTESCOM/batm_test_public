# ATTT – Automated Test Suite for GB ATMs and CAS (using SikuliX)

This repository provides a publicly available automated tests suite for General Bytes ATMs and CAS.

## Overview

General Bytes (GB) has developed the Automated Terminal Testing Tool (ATTT) to help operators efficiently automate
testing of their BATM fleet.  
ATTT ensures error-free, stable operation across various configurations, reducing testing time from days to
hours.

## Use Cases

- Verifying new pre-production BATM software releases
- Automatically checking transaction flows
- Testing negative scenarios and other cases

## Requirements

- **Java Development Kit (JDK) 8** (OpenJDK or Oracle JDK/JRE)
- **SikuliX IDE 2.0.5** ([Download here](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar))

  Officially tested on JDK 8; Java 9+ is supported but may require additional JVM flags
- **64-bit operating system** (Windows, macOS or Linux) — SikuliX supports only 64-bit systems
- **FAT32-formatted USB flash drive**
- **ATTT activation** provided by GB Support

## Security

- Communication with the ATTT server is only possible using unique client certificates issued by GB.
- Certificates must be physically uploaded to each terminal using a FAT32-formatted USB flash drive.

> **Note:** A FAT32-formatted USB flash drive is required to upload certificate to the terminal during activation.

- The ATTT system has been independently security audited.

## Architecture

**Key Components:**

- **ATTT Connector**  
  Streams the terminal’s screen to the ATTT server and processes click events, virtual testing cash insertions, QR
  scans, and
  keyboard events.

- **ATTT Server**  
  Hosted and maintained by GB; enables remote control of terminals via a web browser.  
  [https://attt.generalbytes.com](https://attt.generalbytes.com)

- **SikuliX**  
  Automation tool that lets QA engineers write Python scripts for visual recognition and interaction with terminal
  screens.

## Setup & Activation

> ⚠️ **Warning:**
> This tool is **not recommended** for use on terminals connected to production CAS servers.
> Proceed **at your own risk**.

### Risks

- Sending real cryptocurrency to wallets without any fiat deposited
- Inadvertent dispensing of cash during automated sell flows

### 1. Request Activation

- Contact GB Support to request ATTT server access by providing your terminal serial numbers and user email addresses.
  Support portal: [Create a Support Ticket](https://generalbytes.atlassian.net/wiki/spaces/ESD/pages/934609035)

### 2. Prepare CAS Settings

- Before setting up terminals, configure the following settings in CAS.

#### 2.1.Create a new **AML/KYC Setting:**

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
    - Cash Limit Per Day (For Buy & Sell) = `100000.00`

#### 2.2. Create a new **Fiat Settings:**

- Fiat Currency: **USD - United States dollar**
- **Accept All Banknotes**

#### 2.3. Create a new **Crypto Settings:**

- For each supported currency: **BTC, LBTC, LTC, ETH**.
- Configuration Cash Currency: **USD**.

**Buy Settings:**

- Minimum Buy Cash Amount per Transaction: **100.00**
- Minimum Buy Card Amount per Transaction: **0.00**
- Buy Rate Source: **Demo Rate Source**
- Hot Wallet Buy: **Demo Wallet**
- Exchange Buy: **Demo Exchange**
- Buy Profit (%): **10.00%**
- Fixed Transaction Fee: **10.00**

**Sell Settings (except ETH):**

- Sell Rate Source: **Demo Rate Source**
- Hot Wallet Sell: **Demo Wallet**
- Exchange Sell: **Demo Exchange**
- Sell Strategy - 1: **Receive coins to the Hot Wallet**
- Sell Profit (%): **10.00%**
- Fixed Transaction Fee: **10.00**

> **Note:** ETH does not support sell wallets, thus sell transactions for ETH are not tested.

#### 2.4. Create a new **Discounts:**

- Discount Type: **Discount from fee**
- Set all discount values (`Discount From Buy Profit Fee`, `Discount From Sell Profit Fee`, `Buy Fixed Fee Discount`,
  `Sell Fixed Fee Discount`) to **100.00%**
- Crypto Currencies: **BTC**, **LBTC**, **LTC**, **ETH**
- Configuration Cash Currency - **USD**
- Set **Valid From** and **Valid To** dates to define the period the discount is active (e.g., `01.09.2024` –
  `01.02.2030`)

#### 2.5. Create a new **Locations:**

- Create and select the actual location of your BATM.

### 3. Configure Terminal Details in CAS

#### 3.1. **Custom Strings (on the terminal detail page):**

- Add the `attt` flag to the `special_configuration` custom string.

> ⚠️ **Warning:** Without this flag, ATTT will not work for the terminal!

- Add key-value pairs _(case-sensitive: must match exactly)_:
    - `terms_and_conditions`: **TERMS AND CONDITIONS**
    - `scam_disclaimer`: **SCAM DISCLAIMER**
    - `custom_pep_question`: **PEP QUESTION**
    - `required_disclosures_text`: **REQUIRED DISCLOSURES**
    - `privacy_policy`: **PRIVACY POLICY**
    - `marketing_opt_in_agreement_text`: **Marketing agreement text. Agree?**

#### 3.2. AML/KYC Setting: Select the AML/KYC setting created in step 2.1.

#### 3.3. Fiat Settings: Select the fiat settings created in step 2.2.

#### 3.4. Crypto Settings: Select the crypto settings created in step 2.3.

#### 3.5. Discounts: Select the discounts created in step 2.4.

#### 3.6. Location: Select the location created in step 2.5.

#### 3.7. Main Cash Currency: **USD - United States dollar**

#### 3.8. Crypto Currencies: Select **BTC, LBTC, LTC, ETH**

#### 3.9. **Administration Settings:**

Select the following checkboxes (✓):

- Customer Can Cancel Transaction
- Show Marketing Agreement Screen
- Blur Detection Limit: 1

#### 3.10. **Languages:**

- **Default Language:** en - English
- **Preferred Languages:** cs - Czech, de - German, es - Spanish, ar - Arabic, fi - Finnish, ja - Japanese, fr - French,
  bg - Bulgarian, el - Greek, et - Estonian, hi - Hindi, hr - Croatian, hu - Hungarian, hy - Armenian, it - Italian,
  kk - Kazakh, ko - Korean, lv - Latvian, he - Hebrew, ht - Haitian, ka - Georgian, mk - Macedonian, lt - Lithuanian,
  nl - Dutch, no - Norwegian, pl - Polish, pt - Portuguese, ru - Russian, ro - Romanian, sk - Slovak, sl - Slovenian,
  sr - Serbian, sr - Serbian, th - Thai, tr - Turkish, uk - Ukrainian, vi - Vietnamese, sq - Albanian, zh - Chinese.

#### 3.11. **Printing Settings:**

- Select the following checkboxes (✓):
    - Disable Printer Warnings
- Print Buy Receipt — set value to **Never**
- Print Withdrawal Receipt — set value to **Never**
- Sell Tickets Delivery: set to **None** (to be used with withdrawal using phone number)

> **Tip:** Disabling printer warnings and setting receipt printing to “Never” or “None” helps prevent unwanted paper
> slips from being printed or falling out of the terminal.

#### 3.12. **Publish Settings:**

- The `Publish` checkbox **must NOT** be selected.

#### 3.13. **Terminal Template:**

- You can save all required settings in a Terminal Template and select it in the "Use Terminal Template" field, instead
  of configuring each setting manually.

> **Note:** Reboot the terminal after configuration (recommended, but not required).

### 4. Upload Activation Keys (on the BATM terminal)

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
- Press the button **ENABLE ATTT**.  
  The terminal will now establish a secure connection to the ATTT server.

> ⚠️ The **UPLOAD ATTT KEYS** option will only be visible if the `attt` flag is set in the `special_configuration`
> custom string for this terminal in CAS.

## Running Tests

- Open the ATTT server at [https://attt.generalbytes.com](https://attt.generalbytes.com).
- Click at the **Control terminal** button to access the BATM’s console.
- Clone repository to your local machine:
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
- Tests are optimized for these screen resolutions. Using unsupported resolutions may cause SikuliX visual matching to
  fail.
- Tests are designed and verified on BATM 10 terminals. Other models may require adjustments.
