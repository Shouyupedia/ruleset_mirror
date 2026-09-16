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

- Updated from: `d4f40024c484da56a61a201855b32cba06168186`
- Upstream head: `a3b3588335c7887e16f35f1f4446a26c3aa652c1`
- Time (UTC): 2026-09-16 21:19:57Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1618, changed=4049, add=3141, del=908, base_lines=1252, new_lines=3485)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1615, changed=4049, add=3141, del=908, base_lines=1253, new_lines=3486)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1627, changed=4045, add=3139, del=906, base_lines=1246, new_lines=3479)

<!-- END_GUARD_REPORT -->
