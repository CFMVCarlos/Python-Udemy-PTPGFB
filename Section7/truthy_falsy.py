from typing import Any

false_values: dict[str, Any] = {
    "Empty list": [],
    "Empty dictionary": {},
    "Empty tuple": (),
    "Zero": 0,
    "None": None,
    "False": False,
    "Empty string": "",
    "Empty bytes": b"",
    "Empty bytearray": bytearray(),
    "Empty memoryview": memoryview(b""),
    "Empty set": set(),
    "Empty frozenset": frozenset(),
    "Empty range": range(0),
    "Zero float": 0.0,
    "Zero complex": 0j,
}
for name, value in false_values.items():
    print(f"{name:16}: {bool(value)}")
