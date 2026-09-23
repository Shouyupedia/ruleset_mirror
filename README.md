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

- Updated from: `ea6f4c0ad5792aff34b15e0fa1eea8051432e3be`
- Upstream head: `a502e8aedd3853cd2e50f7eff6695480c1bce868`
- Time (UTC): 2026-09-23 21:31:16Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 12
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1600, changed=3972, add=3072, del=900, base_lines=1252, new_lines=3424)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1597, changed=3972, add=3072, del=900, base_lines=1253, new_lines=3425)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1609, changed=3968, add=3070, del=898, base_lines=1246, new_lines=3418)

<!-- END_GUARD_REPORT -->
