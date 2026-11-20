"""Writes the example year (a 14/14 rotation, days then nights, held over 3 days in
October) into index.html between the year markers. Run after changing the example:
    python3 -I tools/year.py
"""
import datetime
import pathlib
import re

YEAR = 2027
ANCHOR = datetime.date(2026, 12, 20)          # a travel-out day: the cycle's day 0
HELD = {datetime.date(2027, 10, d) for d in (10, 11, 12)}
MOVED_TRAVEL = datetime.date(2027, 10, 13)    # travel home moves after the holdover
LABEL = {"day": "Day shift", "night": "Night shift", "travel": "Travel", "home": "Home", "held": "Held over"}


def kind(d):
    if d in HELD:
        return "held"
    if d == MOVED_TRAVEL:
        return "travel"
    i = (d - ANCHOR).days % 28                # travel, 6 days, 7 nights, travel, 13 home
    if i in (0, 14):
        return "travel"
    return "day" if i <= 6 else "night" if i <= 13 else "home"


def month(m):
    first = datetime.date(YEAR, m, 1)
    cells = [f'<span class="wd">{w}</span>' for w in "MTWTFSS"]
    cells += ['<span class="pad"></span>'] * first.weekday()    # weeks start on Monday
    d = first
    while d.month == m:
        k = kind(d)
        cells.append(f'<span class="d {k}" data-d="{d.isoformat()}">{d.day}</span>')
        d += datetime.timedelta(days=1)
    name = first.strftime("%B")
    return f'<div class="month"><h3>{name}</h3><div class="days">{"".join(cells)}</div></div>'


def base_kind(d):
    """The day before the holdover was saved."""
    i = (d - ANCHOR).days % 28
    if i in (0, 14):
        return "travel"
    return "day" if i <= 6 else "night" if i <= 13 else "home"


def strip():
    """October 4 to 24 before and after the holdover, for the holdover section."""
    days = [datetime.date(YEAR, 10, 4) + datetime.timedelta(days=n) for n in range(21)]
    def row(label, pick):
        cells = "".join(f'<span class="d {pick(d)}" data-d="{d.isoformat()}">{d.day}</span>' for d in days)
        return f'<div class="strip-row"><span class="strip-label">{label}</span><div class="strip-days">{cells}</div></div>'
    return row("Before", base_kind) + "\n" + row("After", kind)


def fill(html, name, block):
    return re.sub(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)", lambda x: f"{x[1]}\n{block}\n{x[2]}", html, flags=re.S)


def main():
    page = pathlib.Path(__file__).resolve().parent.parent / "index.html"
    html = page.read_text()
    html = fill(html, "year", "\n".join(month(m) for m in range(1, 13)))
    html = fill(html, "strip", strip())
    page.write_text(html)


if __name__ == "__main__":
    main()
