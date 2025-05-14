# ATTT – Automated Test Suite for GB ATMs and CAS (using SikuliX)

This repository provides a publicly available tests for General Bytes ATMs and CAS.

## Overview

General Bytes (GB) has developed ATTT to help operators efficiently automate testing of their BATM fleet.  
ATTT ensures error-free, stable operation across a wide range of configurations, reducing testing time from days to hours.

## Use Cases

- Verifying new BATM firmware releases  
- Automatically checking transaction flows  
- Testing negative scenarios and other cases  

## Requirements

- **Java Development Kit (JDK) 8** (OpenJDK or Oracle JDK/JRE) 
> SikuliX is officially tested on Java 8. Java 9+ is also supported but may require additional JVM flags.

- **SikuliX version 2.0.5** ([Download link](https://raiman.github.io/SikuliX1/downloads.html))  
- **64-bit operating system** (Windows, macOS or Linux) — SikuliX supports only 64-bit systems  
- **FAT32-formatted USB flash drive**  
- **ATTT activation** provided by GB Support

## Architecture

**Key Components:**

- **ATTT Connector**  
  Streams the terminal’s screen to the ATTT server and processes click events, virtual cash insertions, QR scans, and keyboard inputs.

- **ATTT Server**  
  Hosted and maintained by GB; enables remote control of terminals via a web browser.  
  [https://attt.generalbytes.com](https://attt.generalbytes.com)

- **SikuliX**  
  Automation tool that lets QA engineers write Python scripts for visual recognition and interaction on terminal screens.

## Setup & Activation

### 1. Request Activation

Submit terminal serial numbers and operator email addresses to GB Support.

### 2. Configure CAS

**Custom Strings:**  
- Add the `attt` flag to the `special_configuration` field.  
- Add the following key-value pairs:  
  - `terms_and_conditions`: **TERMS AND CONDITIONS**  
  - `scam_disclaimer`: **SCAM DISCLAIMER**  
  - `custom_pep_question`: **PEP QUESTION**  
  - `required_disclosures_text`: **REQUIRED DISCLOSURES**  
  - `privacy_policy`: **PRIVACY POLICY**

**Discounts:**  
- Add discounts for **BTC, LBTC, LTC, ETH**.  
- Set the following discount values (each discount should have a value of 100.00%). 
- Configuration Cash Currency - Set default cash currency to **CZK.**

**Crypto Settings:**  
- For each supported currency (**BTC, LBTC, LTC, ETH**):
- Configuration Currencies - Set default cash currency to **CZK.**
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

> **Note:** ETH does not support a sell wallet, so sell transactions for ETH are not configured or tested.

**Printing Settings:**  
- Select the following checkboxes (✓):  
  - Disable Printer Warnings  
- Print Buy Receipt  — set value to **Never**
- Print Withdrawal Receipt — set value to **Never**

**Fiat Settings:**  
- **Fiat Currency:** CZK – Czech koruna  
- **Accept All Banknotes**

**Administration Settings:**  
Select the following checkboxes (✓):  
- Allow Balance Check  
- Allow Voice Call  
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

> ⚠️ Reboot each terminal after completing the configuration.

### 3. Upload Activation Keys

   - Extract the activation ZIP archive to a FAT32-formatted USB drive.  
   - Make sure the file is named **`attt.bks`**.
   - In the Advanced Administration menu, select **UPLOAD ATTT KEYS**.
   - Insert the USB drive into the BATM’s USB port.  
   - After successful upload, a toast notification will confirm the success of the operation.

### 4. Enable ATTT

- Press **ENABLE ATTT** in the Advanced Administration menu.
- The terminal will establish a secure connection to the ATTT server.

## Running Tests

**Clone this repository to your local machine:**

```bash
git clone https://github.com/GENERALBYTESCOM/batm_test_public.git
cd batm_test_public
```

## Security
- All communication uses secure HTTPS WebSocket with unique client certificates issued by GB.  
- Certificates are physically transferred to each terminal via USB.  
- The ATTT system has been independently security audited.


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
