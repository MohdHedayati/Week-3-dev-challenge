# Lazy Inbox Cleaner 🦥📁

An automated background file sorter built for the **Hacktoberfest 2026 Week 3 DEV Challenge** (*Theme: Slow and Steady*).

## 📖 Overview
Are you tired of standing over a cluttered `Downloads` or `Desktop` folder, opening random files, and manually dragging them into subfolders? **Lazy Inbox Cleaner** lets you channel your inner sloth and let AI do the heavy lifting.

It automatically inspects unorganized files in a target directory, analyzes their contents using a fast, lightweight AI model, and organizes them into categorized folders (`Invoices`, `Code`, `Logs`, `Docs`, `Misc`).

## ✨ Features
* **Zero Effort:** Automatically categorizes files based on both filename and internal text snippets.
* **Smart Classification:** Uses Google's Gemini models to distinguish between source code, system logs, invoices, and standard documents.
* **Privacy-Conscious Architecture:** Designed to seamlessly swap to local open-weight models (e.g., Gemma 2 via Ollama) so private documents never leave your machine.
* **Non-Destructive:** Dynamically creates folders and safely handles unknown or uncategorized file types by placing them in `Misc/`.

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* A Google Gemini API Key
