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

- Updated from: `1c5774e7f003cd14c2bc2584c0ff43b636422e0a`
- Upstream head: `348209a429b902602a1d86c7ac8f1522a392be5c`
- Time (UTC): 2026-09-04 11:20:42Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1595, changed=3955, add=3057, del=898, base_lines=1252, new_lines=3411)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1591, changed=3955, add=3057, del=898, base_lines=1253, new_lines=3412)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1598, changed=3949, add=3054, del=895, base_lines=1246, new_lines=3405)

<!-- END_GUARD_REPORT -->
