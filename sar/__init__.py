#!/usr/bin/env python


"""CPU regexp pattern for detecting SAR section header"""
PATTERN_CPU = ".*CPU.*(usr|user).*nice.*sys.*"

"""Regexp terms for finding fields in SAR parts for CPU"""
FIELDS_CPU = [
    '^\%(usr|user)', '^\%nice', '^\%sys', '^\%iowait', '^\%idle'
]

"""Pair regexp terms with field names in CPU output dictionary"""
FIELD_PAIRS_CPU = {
    'usr': FIELDS_CPU[0], 'nice': FIELDS_CPU[1], 'sys': FIELDS_CPU[2],
    'iowait': FIELDS_CPU[3], 'idle': FIELDS_CPU[4]
}

"""Mem usage regexp pattern for detecting SAR section header"""
PATTERN_MEM = '.*kbmemfree.*kbmemused.*memused.*kbbuffers.*kbcached.*'

"""Regexp terms for finding fields in SAR parts for memory usage"""
FIELDS_MEM = [
    '^kbmemfree', '^kbmemused', '^\%memused', '^kbbuffers', '^kbcached'
]

"""Pair regexp terms with field names in memory usage output dictionary"""
FIELD_PAIRS_MEM = {
    'memfreekb': FIELDS_MEM[0], 'memusedkb': FIELDS_MEM[1],
    'memusedpercent': FIELDS_MEM[2], 'membufferkb': FIELDS_MEM[3],
    'memcachekb': FIELDS_MEM[4]
}

"""Swap usage regexp pattern for detecting SAR section header"""
PATTERN_SWP = '.*kbswpfree.*kbswpused.*swpused.*'

"""Regexp terms for finding fields in SAR parts for swap usage"""
FIELDS_SWP = [
    '^kbswpfree', '^kbswpused', '^\%swpused'
]

"""Pair regexp terms with field names in swap usage output dictionary"""
FIELD_PAIRS_SWP = {
    'swapfreekb': FIELDS_SWP[0], 'swapusedkb': FIELDS_SWP[1],
    'swapusedpercent': FIELDS_SWP[2]
}

"""I/O usage regexp pattern for detecting SAR section header"""
PATTERN_IO = '.*tps.*rtps.*wtps.*bread\/s.*bwrtn\/s.*'

"""Regexp terms for finding fields in SAR parts for I/O usage"""
FIELDS_IO = [
    '^tps', '^rtps', '^wtps', '^bread\/s', '^bwrtn\/s'
]

"""Pair regexp terms with field names in I/O usage output dictionary"""
FIELD_PAIRS_IO = {
    'tps': FIELDS_IO[0], 'rtps': FIELDS_IO[1], 'wtps': FIELDS_IO[2],
    'bread': FIELDS_IO[3], 'bwrite': FIELDS_IO[4],
}

"""Task creation and system switching regexp pattern for SAR section header"""
PATTERN_TASK = '.*proc\/s.*cswch\/s.*'

"""Regexp terms for finding fields in SAR parts for task creation and system switching"""
FIELDS_TASK = [
    '^proc\/s', '^cswch\/s'
]

"""Pair regexp terms with field names in Task creation and system switching output dictionary"""
FIELD_PAIRS_TASK = {
    'proc': FIELDS_TASK[0], 'cswch': FIELDS_TASK[1]
}

"""Network usage regexp pattern for SAR section header"""
PATTERN_IFACE = '.*IFACE.*rxpck\/s.*txpck\/s.*rxkB\/s.*txkB\/s.*rxcmp\/s.*txcmp\/s.*rxmcst\/s.*ifutil'

"""Regexp terms for finding fields in SAR parts for network usage"""
FIELDS_IFACE = [
    '^IFACE','^rxpck\/s','^txpck\/s','^rxkB\/s','^txkB\/s','^rxcmp\/s','^txcmp\/s','^rxmcst\/s','^%ifutil'
]

"""Pair regexp terms with field names in network usage dictionary"""
FIELD_PAIRS_IFACE = {
    'iface':FIELDS_IFACE[0], 'rxpck':FIELDS_IFACE[1], 'txpck':FIELDS_IFACE[2], 'rxkB':FIELDS_IFACE[3],
    'txkB':FIELDS_IFACE[4], 'rxcmp':FIELDS_IFACE[5], 'txcmp':FIELDS_IFACE[6], 'rxmcst':FIELDS_IFACE[7],
    'ifutil':FIELDS_IFACE[8]
}

"""Network usage regexp pattern for SAR section header"""
PATTERN_LOAD = '.*runq-sz.*plist-sz.*ldavg-1.*ldavg-5.*ldavg-15.*blocked'

"""Regexp terms for finding fields in SAR parts for network usage"""
FIELDS_LOAD = [
    '^runq-sz','^plist-sz','^ldavg-1','^ldavg-5','^ldavg-15','^blocked'
]

"""Pair regexp terms with field names in network usage dictionary"""
FIELD_PAIRS_LOAD = {
    'runq-sz':FIELDS_IFACE[0], 'plist-sz':FIELDS_IFACE[1], 'ldavg-1':FIELDS_IFACE[2], 'ldavg-5':FIELDS_IFACE[3],
    'ldavg-15':FIELDS_IFACE[4], 'blocked':FIELDS_IFACE[5]
}

"""Restart time regexp pattern for detecting SAR restart notices"""
PATTERN_RESTART = '.*LINUX\ RESTART.*'

"""Pattern for splitting multiple combined SAR file"""
PATTERN_MULTISPLIT = 'Linux'

"""Split by date in multiday SAR file"""
PATTERN_DATE = '[0-9][0-9][0-9][0-9]\-[0-9][0-9]\-[0-9][0-9]'

ALL_PATTERNS = {
    'CPU': {
        'PATTERN': PATTERN_CPU,
        'FIELDS': FIELDS_CPU,
        'PAIRS': FIELD_PAIRS_CPU
    },
    'MEM': {
        'PATTERN': PATTERN_MEM,
        'FIELDS': FIELDS_MEM,
        'PAIRS': FIELD_PAIRS_MEM
    },
    'SWP': {
        'PATTERN': PATTERN_SWP,
        'FIELDS': FIELDS_SWP,
        'PAIRS': FIELD_PAIRS_SWP
    },
    'IO': {
        'PATTERN': PATTERN_IO,
        'FIELDS': FIELDS_IO,
        'PAIRS': FIELD_PAIRS_IO
    },
    'TASK': {
        'PATTERN': PATTERN_TASK,
        'FIELDS': FIELDS_TASK,
        'PAIRS': FIELD_PAIRS_TASK
    },
    'IFACE': {
        'PATTERN': PATTERN_IFACE,
        'FIELDS': FIELDS_IFACE,
        'PAIRS': FIELD_PAIRS_IFACE
    },
    'LOAD': {
        'PATTERN': PATTERN_LOAD,
        'FIELDS': FIELDS_LOAD,
        'PAIRS': FIELD_PAIRS_LOAD
    }
}

__all__ = [
    'PATTERN_RESTART', 'PATTERN_MULTISPLIT',
    'PATTERN_DATE', 'ALL_PATTERNS'
]
