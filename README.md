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

- Updated from: `cc9b4f7f029328d8638d0d7335d129b092cfd45b`
- Upstream head: `e6cc7d8268d5308a3b6762dc779aef37cdb91c11`
- Time (UTC): 2026-09-15 04:56:53Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 12
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1617, changed=4053, add=3145, del=908, base_lines=1252, new_lines=3489)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1613, changed=4053, add=3145, del=908, base_lines=1253, new_lines=3490)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1625, changed=4049, add=3143, del=906, base_lines=1246, new_lines=3483)

<!-- END_GUARD_REPORT -->
