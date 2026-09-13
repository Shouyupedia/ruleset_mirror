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

- Updated from: `4f60269072636d3caf53273421d67fc3d23e40cd`
- Upstream head: `d6a7e0f970c7bf26de058329c2d75ac5cb76b150`
- Time (UTC): 2026-09-13 11:55:37Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 26
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1628, changed=4042, add=3133, del=909, base_lines=1252, new_lines=3476)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1625, changed=4042, add=3133, del=909, base_lines=1253, new_lines=3477)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1637, changed=4038, add=3131, del=907, base_lines=1246, new_lines=3470)

<!-- END_GUARD_REPORT -->
