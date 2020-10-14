#!/usr/bin/env python

"""
PMM 2.x Client Docker container.

It runs pmm-agent as a process with PID 1.
It is configured entirely by environment variables. Arguments or flags are not used.

The following environment variables are recognized by the Docker entrypoint:
* PMM_AGENT_ENTRYPOINT_DELAY - if non-zero, entrypoint execution is delayed for a given number of seconds.
* PMM_AGENT_SETUP            - if true, `pmm-agent setup` is called before `pmm-agent run`.

Additionally, the many environment variables are recognized by pmm-agent itself.
The following help text shows them as [PMM_AGENT_XXX].
"""

from __future__ import print_function, unicode_literals
import os
import sys
import time
from distutils.util import strtobool


PMM_AGENT_ENTRYPOINT_DELAY = int(os.environ.get('PMM_AGENT_ENTRYPOINT_DELAY', '0'))
PMM_AGENT_SETUP            = strtobool(os.environ.get('PMM_AGENT_SETUP', 'false'))


def main():
    """
    Entrypoint.
    """

    if len(sys.argv) > 1:
        print(__doc__, file=sys.stderr)
        os.system('pmm-agent setup --help')
        sys.exit(1)

    if PMM_AGENT_ENTRYPOINT_DELAY:
        print('Sleeping {} second(s) ...'.format(PMM_AGENT_ENTRYPOINT_DELAY), file=sys.stderr)
        time.sleep(PMM_AGENT_ENTRYPOINT_DELAY)

    if PMM_AGENT_SETUP:
        print('Starting pmm-agent setup ...', file=sys.stderr)
        status = os.system('pmm-agent setup')
        if status != os.EX_OK:
            sys.exit(status)

    print('Starting pmm-agent ...', file=sys.stderr)
    sys.stderr.flush()

    # use execlp to replace the current process (this entrypoint)
    # with pmm-agent with inherited environment
    os.execlp('pmm-agent', 'run')


if __name__ == '__main__':
    main()