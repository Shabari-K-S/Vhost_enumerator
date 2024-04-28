# Vhost Enumerator

## Introduction
The Vhost Enumerator is a tool used for enumerating virtual hosts on a target web server. It helps in identifying all the subdomains configured on the server, which can be useful for various purposes such as security assessments, bug bounty hunting, or web application testing.

## Features
- Enumerate subdomain on a target web server
- Customizable options for fine-tuning the enumeration process

## Installation
1. Clone the repository: `git clone https://github.com/Shabari-K-S/vhost_enumerator`
2. Change to the project directory: `cd vhost-enumerator`
3. Install the required dependencies: `./install.sh`

## Usage
To use the Vhost Enumerator, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the following command to start the enumeration process:
    ```
    python vhost_enumerator.py --url <target_url> --wordlist <wordlist_file>
    ```
    Replace `<target_url>` with the URL of the target web server and `<wordlist_file>` with the path to the wordlist file containing the list of virtual hosts to check.
3. Wait for the enumeration process to complete.
4. View the results in the specified output format.

## Options
The Vhost Enumerator supports the following options:

- `--url <target_url>`: Specify the target URL of the web server.
- `--wordlist <wordlist_file>`: Specify the path to the wordlist file containing the list of virtual hosts to check.

## Examples
Here are some examples of how to use the Vhost Enumerator:

- Enumerate virtual hosts on a single target URL:
  ```
  python vhost_enumerator.py --url https://SCAN.example.com --wordlist wordlist.txt
  ```
- Enumerate virtual hosts on single target URLs in different way:
  ```
  python vhost_enumerator.py -u https://SCAN.example.com -w wordlist.txt
  ```

