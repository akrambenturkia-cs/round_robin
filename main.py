import sys
from contextlib import redirect_stdout

from src.simulator import run_simulation


class ColorizedOutput:
    RESET = "\033[0m"
    COLORS = {
        "title": "\033[1;36m",
        "request": "\033[32m",
        "unavailable": "\033[31m",
        "statistics": "\033[1;35m",
        "server": "\033[33m",
    }

    def __init__(self, stream):
        self.stream = stream
        self.enabled = stream.isatty()
        self.buffer = ""

    def write(self, text):
        self.buffer += text
        while "\n" in self.buffer:
            line, self.buffer = self.buffer.split("\n", 1)
            self._write_line(f"{line}\n")
        return len(text)

    def flush(self):
        if self.buffer:
            self._write_line(self.buffer)
            self.buffer = ""
        self.stream.flush()

    def _write_line(self, line):
        color = self._color_for(line)
        if self.enabled and color:
            self.stream.write(f"{color}{line}{self.RESET}")
        else:
            self.stream.write(line)

    def _color_for(self, line):
        if line.startswith("ROUND ROBIN"):
            return self.COLORS["title"]
        if line.startswith("Request ") and "No available server" in line:
            return self.COLORS["unavailable"]
        if line.startswith("Request "):
            return self.COLORS["request"]
        if line.startswith("======== Load Balancer Statistics"):
            return self.COLORS["statistics"]
        if line.startswith("Server: "):
            if "Percentage: 100.00%" in line:
                return self.COLORS["unavailable"]
            return self.COLORS["server"]
        return ""


if __name__ == "__main__":
    output = ColorizedOutput(sys.stdout)
    try:
        with redirect_stdout(output):
            run_simulation()
    finally:
        output.flush()
