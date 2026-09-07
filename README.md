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

- Updated from: `0e7da65eec9809c755a3167f479711b9c6337111`
- Upstream head: `b067ff30f4b3cb5e5d00cf1e27752db3477d8e7b`
- Time (UTC): 2026-09-07 12:37:04Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 17
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1592, changed=3962, add=3064, del=898, base_lines=1252, new_lines=3418)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1588, changed=3962, add=3064, del=898, base_lines=1253, new_lines=3419)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1594, changed=3956, add=3061, del=895, base_lines=1246, new_lines=3412)

<!-- END_GUARD_REPORT -->
