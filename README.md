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

- Updated from: `814e22769abab552e03d16bbb7df74189f791656`
- Upstream head: `730962ec2f1ea8c07697150dc7caa09029cf43e5`
- Time (UTC): 2026-09-03 11:17:25Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1595, changed=3954, add=3056, del=898, base_lines=1252, new_lines=3410)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1592, changed=3954, add=3056, del=898, base_lines=1253, new_lines=3411)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1598, changed=3948, add=3053, del=895, base_lines=1246, new_lines=3404)

<!-- END_GUARD_REPORT -->
