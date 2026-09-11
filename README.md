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

- Updated from: `71127b25d023cebd362a7279552a338e8c394578`
- Upstream head: `237bd96c062b7e2854811cf44e1543ba806b51b9`
- Time (UTC): 2026-09-11 20:59:10Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1623, changed=4040, add=3132, del=908, base_lines=1252, new_lines=3476)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1619, changed=4040, add=3132, del=908, base_lines=1253, new_lines=3477)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1631, changed=4036, add=3130, del=906, base_lines=1246, new_lines=3470)

<!-- END_GUARD_REPORT -->
