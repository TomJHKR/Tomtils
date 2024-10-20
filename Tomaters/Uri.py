import re
from typing import Optional

# Based on regex from RFC 3986:
# https://datatracker.ietf.org/doc/html/rfc3986#appendix-B
URI_PATTERN = re.compile(r"^(([^:/?#]+):)?(//([^/?#]*))?([^?#]*)(\?([^#]*))?(#(.*))?")


def extract_scheme(s: str) -> Optional[str]:
    matches = re.search(URI_PATTERN, s)

    # Return scheme if matches
    if matches:
        return matches.group(2).lower()
