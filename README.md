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

- Updated from: `442d2732dc8b41592a7f380997e7f4c43a45d033`
- Upstream head: `b41911111f00e24000a00e8f8809a472559e1781`
- Time (UTC): 2026-09-10 11:22:42Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 25
- Added files: 5
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1629, changed=4041, add=3132, del=909, base_lines=1252, new_lines=3475)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1625, changed=4041, add=3132, del=909, base_lines=1253, new_lines=3476)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1637, changed=4037, add=3130, del=907, base_lines=1246, new_lines=3469)

<!-- END_GUARD_REPORT -->
