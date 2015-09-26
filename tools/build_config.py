#!/usr/bin/env python
from __future__ import print_function

import json
import sys

base = {
    "max-concurrent-indexers" : 1,
    "dbpath" : "/hound/data",
}

poll_ms = 1000 * 60 * 30


def build_repo(name):
    return (
        name,
        {
            "url": "https://github.com/%s.git" % name,
            "ms-between-poll": poll_ms,
        },
    )

def main():
    config = dict(base)
    config['repos'] = dict(build_repo(repo.strip()) for repo in sys.stdin)
    print(json.dumps(config, sort_keys=True, indent=4))


if __name__ == "__main__":
    main()
