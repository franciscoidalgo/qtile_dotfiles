
import re
import subprocess

from libqtile.widget import base


def make_it_cooler(indicator):
    indicator_as_list = list(indicator)
    indicator_as_list[0] = indicator_as_list[0].replace(
        "Num", "").replace("Caps", "בּ")
    return tuple(indicator_as_list)


class CustomLock(base.ThreadPoolText):
    """Really simple widget to show the current Caps/Num Lock state."""

    defaults = [("update_interval", 0.5, "Update Time in seconds.")]

    def __init__(self, **config):
        base.ThreadPoolText.__init__(self, "", **config)
        self.add_defaults(CustomLock.defaults)

    def get_indicators(self):
        """Return a list with the current state of the keys."""
        try:
            output = self.call_process(["xset", "q"])
        except subprocess.CalledProcessError as err:
            output = err.output
            return []
        if output.startswith("Keyboard"):
            indicators = re.findall(r"(Caps|Num)\s+Lock:\s*(\w*)", output)
            return indicators

    def poll(self):
        """Poll content for the text box."""
        indicators = self.get_indicators()
        indicators = list(map(make_it_cooler, indicators))
        status = " ".join([" ".join(indicator) for indicator in indicators])
        return status
