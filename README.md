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

- Updated from: `49f4d177a482dee60dfccd0fdf3f804ea029814f`
- Upstream head: `8bcd5b0eb34c7c6217cf6c23a4b1c1d01f088947`
- Time (UTC): 2026-09-28 05:26:58Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 8

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1597, changed=3980, add=3080, del=900, base_lines=1252, new_lines=3432)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5152, changed=17, add=14, del=3, base_lines=22, new_lines=33)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5312, changed=17, add=14, del=3, base_lines=21, new_lines=32)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1593, changed=3980, add=3080, del=900, base_lines=1253, new_lines=3433)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5152, changed=17, add=14, del=3, base_lines=22, new_lines=33)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5312, changed=17, add=14, del=3, base_lines=21, new_lines=32)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1605, changed=3976, add=3078, del=898, base_lines=1246, new_lines=3426)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.5185, changed=14, add=12, del=2, base_lines=17, new_lines=27)

<!-- END_GUARD_REPORT -->
