#!/usr/bin/env python3
"""
tiny_toolbox.py — a small CLI that logs notes, shows stats, and deletes notes.
Standard library only.
"""
from __future__ import annotations
import argparse, json, os, statistics, sys, time
from pathlib import Path

DB = Path.home() / ".tiny_toolbox_data.json"

def load_notes() -> list[dict]:
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8") or "[]")
    return []

def save_notes(notes: list[dict]) -> None:
    DB.write_text(json.dumps(notes, indent=4), encoding="utf-8")

def cmd_add(text: str) -> None:
    notes = load_notes()
    notes.append({"timestamp": int(time.time()), "content": text})
    save_notes(notes)
    print(f"Added entry #{len(notes)}")

def cmd_list(limit: int) -> None:
    notes = load_notes()[:limit]
    for i, n in enumerate(notes, 1):
        ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n["timestamp"]))
        print(f"{i}. ({ts}) {n['content']}")

def cmd_delete(index: int) -> None:
    notes = load_notes()
    if 0 < index <= len(notes):
        removed = notes.pop(index - 1)
        save_notes(notes)
        print(f"Deleted: {removed['content']}")
    else:
        print("Invalid index")

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="tiny_toolbox")
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("add"); a.add_argument("text")
    l = sub.add_parser("list"); l.add_argument("-n", type=int, default=5)
    d = sub.add_parser("delete"); d.add_argument("index", type=int)
    sub.add_parser("stats")
    args = p.parse_args(argv)
    if args.cmd == "add": cmd_add(args.text)
    elif args.cmd == "list": cmd_list(args.n)
    elif args.cmd == "delete": cmd_delete(args.index)
    else:
        notes = load_notes()
        print(f"Total entries: {len(notes)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
