# OBS-AutoSegment

**OBS-AutoSegment** is a Python script for OBS Studio that automatically segments recordings into fixed time intervals. It helps avoid oversized video files and minimizes the risk of losing entire sessions due to file corruption.

## 🔧 Features

- Automatically starts recording
- Splits recordings into chunks (default: every 30 minutes)
- Runs entirely within OBS Studio’s scripting interface
- Logs recording status and session count
- Lightweight and does not require external dependencies

## 📦 Requirements

- **OBS Studio** (Tested on 29+)
- **Python 3.6+**
- OBS must be configured to allow scripting with Python (check OBS > Tools > Scripts)

## 📁 Installation

1. Open OBS Studio
2. Go to `Tools` > `Scripts`
3. Click `+` and add the `Loop Start/Stop` file
4. Set your desired interval (in minutes)
5. Click “Start Loop” to begin automatic segmented recording

## ❌ How to stop the loop

1. Click the `Loop Start/Stop` button again

## ⚙️ Configuration

- **Interval (minutes):** Sets how often the recording should be saved and restarted
- **Start/Stop Loop:** Buttons to control the automated loop

> **Note:** The OBS scripting interface does not dynamically update button labels, so visibility is toggled between the Start and Stop buttons.

## 📝 Logs

All actions are logged to the OBS script log.  
You can view them via:  
`Help` > `Log Files` > `View Current Log` or by checking the script log panel.

Example log output:
```
\[AutoRec] Loop iniciado.
\[AutoRec] Iniciando gravação...
\[AutoRec] Parando gravação...
\[AutoRec] Vídeos gravados nesta sessão: 3
```

## 📌 Limitations

- The OBS scripting UI has limited dynamic capabilities. Button labels don’t update in real time.
- Logs are only visible in the OBS log window.
- This script is meant for local use, not for streaming control.

## 💡 Use Case

Ideal for:
- Long recording sessions (e.g., podcasts, gameplays, lectures)
- Preventing total data loss from corrupt files
- Easier file management with segmented clips

## 📄 License

MIT License – use freely, modify as needed, contributions welcome.

## 🤝 Contribute

Feel free to fork, improve or report issues.  
For suggestions or collaboration, open an issue or contact me.

