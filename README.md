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

- Updated from: `4c34e4784d76dc715af98cc11e5d434cc3529d0a`
- Upstream head: `864f0b047a8f1e79244edbd6082dd9666c7412fd`
- Time (UTC): 2026-08-26 20:02:58Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 21
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1567, changed=3985, add=3089, del=896, base_lines=1252, new_lines=3445)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1564, changed=3985, add=3089, del=896, base_lines=1253, new_lines=3446)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1570, changed=3979, add=3086, del=893, base_lines=1246, new_lines=3439)

<!-- END_GUARD_REPORT -->
