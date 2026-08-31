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

- Updated from: `799d5b2fedb8ccb686a17c14974e3f5301f76dad`
- Upstream head: `948e9b5b3eb494a6d4b96881fb02409a5c21e6d0`
- Time (UTC): 2026-08-31 22:52:19Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1588, changed=3956, add=3059, del=897, base_lines=1252, new_lines=3414)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1584, changed=3956, add=3059, del=897, base_lines=1253, new_lines=3415)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1590, changed=3950, add=3056, del=894, base_lines=1246, new_lines=3408)

<!-- END_GUARD_REPORT -->
