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

- Updated from: `7692399e89f0d8405e0cdc0a388ddf5ae7063bcb`
- Upstream head: `c4170b1e2a0b1f84d18e99ee233fac776a8da1d1`
- Time (UTC): 2026-09-05 15:16:16Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 12
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1594, changed=3956, add=3058, del=898, base_lines=1252, new_lines=3412)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1591, changed=3956, add=3058, del=898, base_lines=1253, new_lines=3413)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1597, changed=3950, add=3055, del=895, base_lines=1246, new_lines=3406)

<!-- END_GUARD_REPORT -->
