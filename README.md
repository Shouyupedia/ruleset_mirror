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

- Updated from: `a0285b31eab5110c6da3916567b82ad764c01f0c`
- Upstream head: `db917c7a516a0fb48ba016cf85436d11598da942`
- Time (UTC): 2026-09-04 04:36:43Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1595, changed=3954, add=3056, del=898, base_lines=1252, new_lines=3410)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1592, changed=3954, add=3056, del=898, base_lines=1253, new_lines=3411)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1598, changed=3948, add=3053, del=895, base_lines=1246, new_lines=3404)

<!-- END_GUARD_REPORT -->
