# ruleset mirror

## Binary rule sets

GitHub Actions compiles supported sources alongside the original files:

- `Clash/domainset/*.txt` becomes domain-behavior `*.mrs`.
- CIDR-only `Clash/ip/*.txt` becomes ipcidr-behavior `*.mrs`.
- `sing-box/{domainset,non_ip,ip}/*.json` becomes `*.srs`.

Mihomo MRS does not support classical rule sets. `Clash/non_ip` and IP files
containing unsupported rules such as `IP-ASN` remain available in source form
and are not converted into incomplete binaries.

Human pushes to matching source paths trigger the compiler directly. Scheduled
upstream synchronization calls the same reusable compiler explicitly after its
source commit is pushed, because pushes made with `GITHUB_TOKEN` do not create
another push-triggered workflow run.

<!-- BEGIN_GUARD_REPORT -->
## Auto Update Guard Report

- Updated from: `9af16ed88be15718389312c8914f154e39061136`
- Upstream head: `92b47a7704b6b7d7b1e68467ba30930fce33670c`
- Time (UTC): 2026-09-09 20:57:14Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1597, changed=3964, add=3065, del=899, base_lines=1252, new_lines=3418)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1594, changed=3964, add=3065, del=899, base_lines=1253, new_lines=3419)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1600, changed=3958, add=3062, del=896, base_lines=1246, new_lines=3412)

<!-- END_GUARD_REPORT -->
