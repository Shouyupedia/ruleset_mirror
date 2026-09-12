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

- Updated from: `7d6b2ce3b1464e1b7975d61db39036748ee9e19a`
- Upstream head: `65c438c827a7a31639400cd00678c8bd339a3577`
- Time (UTC): 2026-09-12 15:33:30Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1622, changed=4042, add=3134, del=908, base_lines=1252, new_lines=3478)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1618, changed=4042, add=3134, del=908, base_lines=1253, new_lines=3479)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1630, changed=4038, add=3132, del=906, base_lines=1246, new_lines=3472)

<!-- END_GUARD_REPORT -->
