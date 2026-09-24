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

- Updated from: `14d6a14db1a70b348dbdb8e6eb70ec21d5a99be6`
- Upstream head: `3d80b08b76a3ec9f90107336b5faa7c6f855b950`
- Time (UTC): 2026-09-24 11:49:03Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1600, changed=3972, add=3072, del=900, base_lines=1252, new_lines=3424)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1597, changed=3972, add=3072, del=900, base_lines=1253, new_lines=3425)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1609, changed=3968, add=3070, del=898, base_lines=1246, new_lines=3418)

<!-- END_GUARD_REPORT -->
