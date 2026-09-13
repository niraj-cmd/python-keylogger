# ⌨️ Windows Keyboard Event Monitoring Lab

> ⚠️ **Educational & Authorized Security Research Only**

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/API-Windows%20API-555555?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Purpose-Security%20Research-red?style=for-the-badge" />
</p>

<p align="center">
  <b>🔬 Windows Security Research • Python • Windows API • Keyboard Event Monitoring</b>
</p>

---

## 🧬 About

A Python-based Windows security research project demonstrating how Python can interact with the Windows API to observe keyboard-event state.

The project uses `ctypes` and the Windows `GetAsyncKeyState()` API to examine virtual-key states, detect key transitions, convert selected keys into readable representations, buffer events, and demonstrate HTTP communication through a configured Discord webhook.

---

## ✨ Features

- 🪟 Windows API integration using Python `ctypes`
- ⌨️ Virtual-key state monitoring
- 🔄 Key press transition detection
- 🧵 Background worker thread
- 🔒 Thread-safe event buffering
- 📦 JSON payload generation
- 🌐 HTTP POST communication
- 🐍 Python standard-library implementation
- 🧪 Controlled cybersecurity research

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| 🐍 Python 3 | Main programming language |
| 🪟 Windows API | Keyboard-state interaction |
| `ctypes` | Native Windows API access |
| `threading` | Background processing |
| `urllib.request` | HTTP communication |
| `json` | Payload generation |

---

## 🔍 How It Works

```text
          ┌─────────────────────┐
          │   Windows Keyboard  │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  GetAsyncKeyState() │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  Key State Tracking │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  Event Buffer       │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Background Thread   │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  JSON / HTTP POST   │
          └─────────────────────┘
