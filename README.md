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

- Updated from: `a590180c8c26335a2de40fe80733a56c37c6777a`
- Upstream head: `0d96d2c5328d20bbbed3c6f7071511f50015ba60`
- Time (UTC): 2026-10-07 06:03:42Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 12
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 8

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1582, changed=4011, add=3111, del=900, base_lines=1252, new_lines=3463)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1579, changed=4011, add=3111, del=900, base_lines=1253, new_lines=3464)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1591, changed=4007, add=3109, del=898, base_lines=1246, new_lines=3457)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.5185, changed=14, add=12, del=2, base_lines=17, new_lines=27)

<!-- END_GUARD_REPORT -->
