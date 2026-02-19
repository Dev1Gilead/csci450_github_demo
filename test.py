#!/usr/bin/env python3
"""
tiny_toolbox.py — a small CLI that logs notes, shows stats, and makes a quick plot.
Standard library only.
"""
from __future__ import annotations
import argparse, json, os, random, statistics, sys, time
from pathlib import Path

DB = Path.home() / ".tiny_toolbox_notes.json"

def load_notes() -> list[dict]:
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8") or "[]")
    return []

def save_notes(notes: list[dict]) -> None:
    DB.write_text(json.dumps(notes, indent=2), encoding="utf-8")

def cmd_add(text: str) -> None:
    notes = load_notes()
    notes.append({"t": int(time.time()), "text": text})
    save_notes(notes)
    print(f"Saved note #{len(notes)}")

def cmd_list(limit: int) -> None:
    notes = load_notes()[-limit:]
    for i, n in enumerate(notes, 1):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n["t"]))
        print(f"{i:>2}. [{ts}] {n['text']}")

def cmd_stats() -> None:
    notes = load_notes()
    lengths = [len(]()