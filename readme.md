---------------------------------------
# **Welcome**

## About This Project 🚀

**Tomtils** is your one-stop-shop, all-in-one, space-saving, universal, compact, do-it-all, versatile multitool for Security Operations Center (SOC) Analysts. 
With a wide range of utilities for various network security tasks, Tomtils helps streamline operations, automate repetitive tasks, and provide quick access to critical tools for threat analysis and response.

**Tomtils** is a **hobby project** that I work on in my spare time. The goal is to create a versatile and compact toolset for SOC analysts. As this is an ongoing project, **methods and features will be added over time** as new ideas come up or based on suggestions from users. Feel free to reach out with any feature requests or ideas, and I'll do my best to integrate them!

### *Actions* ⚙️
- *Tomaters* 🍅:
    - `fang` - This is used to fang an input 🔒
    - `defang` - Used to defang your variables 🐍
    - `redact` - Redacts a string/list ✂️
    - `decode64` - Decode base64 🔑
    - `encode64` - Encode base64 🔐
    - `iprange` - Given an IP range (e.g., `100.224.0.0/12`), generates a single-column CSV of all IPs in the subnet 🌐
- *Tueries* 🔎:
    - `scan` - Automatically determines if the input is an IP, URL, or hash and performs the corresponding scan below 🖧
        - `searchIP` - Use VirusTotal to scan IPs (needs VTKEY, limited to 4 per minute) 🕵️‍♂️
        - `searchURL` - Use VirusTotal to scan URLs (needs VTKEY, limited to 4 per minute) 🌐
        - `searchHash` - Use VirusTotal to scan hashes (needs VTKEY, limited to 4 per minute) 🔍
    - `concat` - Used to concatenate large queries from a list 🔗
    - `port` - Enter a port number to see information about that port 📡
    - `lolbas` - Query .EXE's and .DLL's against the LOLBAS database 🖥️
- *Tothers* 🔧:
    - `writetxt` - Write history log to a text file 📜
    - `hist` - List all processed versions of your input 📝
    - `use <name>` - Change the input to process to an item from the history list 🔄
    - `change` - Change the working input entirely 🔄
    - `help` - Self explanatory ❓
    - `exit` - Self explanatory 🚪

## Installation 🛠️

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Tomtils.git
    cd Tomtils
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```
## Usage 🖥️

### Command-Line Arguments 📜

- **`-m` / `--method`**: The method to execute (e.g., `decode64`, `fang`).
- **`-i` / `--input`**: (Optional) The input for the method.

### Example Commands:

#### 1. Defang a string:

```bash
python main.py -m defang -i "http://example.com"
```

This will defang the input string `"http://example.com"` by replacing `"http"` with `"hxxp"` and `"."` with `"[.]"`.

#### 2. Encode a string to Base64:

```bash
python main.py -m encode64 -i "hello"
```

This will Base64 encode the string `"hello"`.

#### 3. Search an IP on VirusTotal:

```bash
python main.py -m scan -i "8.8.8.8"
```

This will use VirusTotal to search for the IP `"8.8.8.8"` (requires VirusTotal API key).

#### 4. Run interactively:

```bash
python main.py
```

### History Management 🕒

- **`hist`**: View all previous inputs.
- **`writetxt`**: Save the current history to a text file.

## Development 💻

**Contributions are welcome**, although I may rewrite suggestions in my own way to maintain the overall vision and consistency of the project. Feel free to reach out with any feature requests or ideas, and I'll do my best to integrate them!

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---------------------------------------

