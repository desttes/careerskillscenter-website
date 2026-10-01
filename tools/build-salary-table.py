#!/usr/bin/env python3
"""Fill the "Pay in every state" table in the salary blog post.

Reads the BLS OEWS state file (state_M2025_dl.xlsx, from oesm25st.zip at
https://www.bls.gov/oes/tables.htm) and rewrites everything between
<!-- STATE-TABLE:START --> and <!-- STATE-TABLE:END --> in tools/build-pages.py
(the post's PAGES.append block). Then run tools/build-pages.py to regenerate the page.

Usage (yearly update):
    python3 tools/build-salary-table.py path/to/state_M2025_dl.xlsx
    python3 tools/build-pages.py

Columns: State | coders median/yr (29-2072 A_MEDIAN) | coders median/hr (29-2072 H_MEDIAN)
         | billers median/yr (43-3021 A_MEDIAN) | coding jobs (29-2072 TOT_EMP).
Rows: 50 states + DC (AREA_TYPE 2), alphabetical; Puerto Rico, Guam and the Virgin
Islands are left out. BLS symbols: "*" / "**" = not published; "#" = at or above the
top-coded wage ($239,200 a year / $115.00 an hour).
Needs: pip install openpyxl
"""
import re
import sys
from pathlib import Path

import openpyxl

TARGET = Path(__file__).with_name("build-pages.py")
SKIP = {"Puerto Rico", "Guam", "Virgin Islands"}
START, END = "<!-- STATE-TABLE:START -->", "<!-- STATE-TABLE:END -->"
NA = "Not published"
CAPTION = "Median pay by state, May 2025. Source: U.S. Bureau of Labor Statistics."


def money(v, hourly=False):
    if v == "#":
        return "$115.00 or more" if hourly else "$239,200 or more"
    if isinstance(v, (int, float)):
        return f"${v:,.2f}" if hourly else f"${v:,.0f}"
    return NA  # "*", "**", blank


def count(v):
    return f"{v:,.0f}" if isinstance(v, (int, float)) else NA


def load(path):
    ws = openpyxl.load_workbook(path, read_only=True, data_only=True).worksheets[0]
    rows = ws.iter_rows(values_only=True)
    hdr = next(rows)
    data = {}
    for r in rows:
        d = dict(zip(hdr, r))
        if str(d["AREA_TYPE"]) != "2" or d["AREA_TITLE"] in SKIP:
            continue
        if d["OCC_CODE"] in ("29-2072", "43-3021"):
            data.setdefault(d["AREA_TITLE"], {})[d["OCC_CODE"]] = d
    return data


def build(data):
    lines = [
        '        <div class="table-wrap">',
        '        <table class="data-table">',
        f"          <caption>{CAPTION}</caption>",
        "          <thead>",
        "            <tr><th>State</th><th>Coders: median per year</th><th>Coders: median per hour</th>"
        "<th>Billers: median per year</th><th>Number of coding jobs</th></tr>",
        "          </thead>",
        "          <tbody>",
    ]
    for state in sorted(data):
        c, b = data[state]["29-2072"], data[state]["43-3021"]
        lines.append(
            f"            <tr><td>{state}</td><td>{money(c['A_MEDIAN'])}</td>"
            f"<td>{money(c['H_MEDIAN'], True)}</td><td>{money(b['A_MEDIAN'])}</td>"
            f"<td>{count(c['TOT_EMP'])}</td></tr>")
    lines += ["          </tbody>", "        </table>", "        </div>"]
    return "\n".join(lines)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    data = load(sys.argv[1])
    if len(data) != 51:
        sys.exit(f"expected 50 states + DC, found {len(data)}")
    src = TARGET.read_text(encoding="utf-8")
    pat = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    if len(pat.findall(src)) != 1:
        sys.exit(f"need exactly one {START} ... {END} block in {TARGET.name}")
    src = pat.sub(lambda m: f"{START}\n{build(data)}\n        {END}", src)
    TARGET.write_text(src, encoding="utf-8")
    print(f"wrote {len(data)} rows into {TARGET.name}")


if __name__ == "__main__":
    main()
