"""Validate the checked-in social cover without rerendering platform fonts."""

from pathlib import Path
from struct import unpack

cover = Path(__file__).resolve().parents[1] / "assets" / "social" / "og-cover.png"
data = cover.read_bytes()
assert data[:8] == b"\x89PNG\r\n\x1a\n", "Invalid social cover PNG"
assert data[12:16] == b"IHDR", "Missing social cover dimensions"
assert unpack(">II", data[16:24]) == (1200, 630), "Unexpected social cover dimensions"
print("Social cover asset verified: 1200x630 PNG")
