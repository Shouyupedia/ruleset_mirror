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

- Updated from: `9687ff4ac8d8e550a827912b144e83114b5e49f5`
- Upstream head: `0acc6ca05e2777e0f473e6204d210fdcd6573bc5`
- Time (UTC): 2026-11-17 07:57:22Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 13

### Skipped file list
- `Clash/ip/ai.txt` (ratio=0.9227, changed=394, add=390, del=4, base_lines=41, new_lines=427)
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1778, changed=4067, add=3134, del=933, base_lines=1252, new_lines=3453)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5556, changed=20, add=17, del=3, base_lines=22, new_lines=36)
- `LegacyClashPremium/ip/ai.txt` (ratio=0.9249, changed=394, add=390, del=4, base_lines=40, new_lines=426)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5714, changed=20, add=17, del=3, base_lines=21, new_lines=35)
- `List/ip/ai.conf` (ratio=0.9227, changed=394, add=390, del=4, base_lines=41, new_lines=427)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1775, changed=4067, add=3134, del=933, base_lines=1253, new_lines=3454)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5556, changed=20, add=17, del=3, base_lines=22, new_lines=36)
- `Surfboard/ip/ai.conf` (ratio=0.9249, changed=394, add=390, del=4, base_lines=40, new_lines=426)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5714, changed=20, add=17, del=3, base_lines=21, new_lines=35)
- `sing-box/ip/ai.json` (ratio=0.9238, changed=388, add=387, del=1, base_lines=34, new_lines=420)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1787, changed=4063, add=3132, del=931, base_lines=1246, new_lines=3447)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.6061, changed=20, add=18, del=2, base_lines=17, new_lines=33)

<!-- END_GUARD_REPORT -->
