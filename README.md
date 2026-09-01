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

- Updated from: `a823774660816ec15a85068741b841f50d6259d6`
- Upstream head: `607d73a02214615691d2750eba072fb0c5b7dfe4`
- Time (UTC): 2026-09-01 21:03:22Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1588, changed=3956, add=3059, del=897, base_lines=1252, new_lines=3414)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1584, changed=3956, add=3059, del=897, base_lines=1253, new_lines=3415)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1590, changed=3950, add=3056, del=894, base_lines=1246, new_lines=3408)

<!-- END_GUARD_REPORT -->
