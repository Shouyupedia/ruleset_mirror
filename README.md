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

- Updated from: `9f6c5dc360229d39b51c919a7fe4e1953dcc785c`
- Upstream head: `2416691ff9ce88982e733be62838426a1354b61a`
- Time (UTC): 2026-09-22 21:21:10Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 25
- Added files: 5
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1601, changed=3970, add=3070, del=900, base_lines=1252, new_lines=3422)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1598, changed=3970, add=3070, del=900, base_lines=1253, new_lines=3423)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1610, changed=3966, add=3068, del=898, base_lines=1246, new_lines=3416)

<!-- END_GUARD_REPORT -->
