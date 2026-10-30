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

- Updated from: `4b06132f1fda8ac76f51956467b3a2221c52095a`
- Upstream head: `200821f295041714fa9f4a6bfb68b74c6899b8fb`
- Time (UTC): 2026-10-30 22:23:27Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 13

### Skipped file list
- `Clash/ip/ai.txt` (ratio=0.9211, changed=385, add=381, del=4, base_lines=41, new_lines=418)
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1598, changed=4050, add=3145, del=905, base_lines=1252, new_lines=3492)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `LegacyClashPremium/ip/ai.txt` (ratio=0.9233, changed=385, add=381, del=4, base_lines=40, new_lines=417)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `List/ip/ai.conf` (ratio=0.9211, changed=385, add=381, del=4, base_lines=41, new_lines=418)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1595, changed=4050, add=3145, del=905, base_lines=1253, new_lines=3493)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `Surfboard/ip/ai.conf` (ratio=0.9233, changed=385, add=381, del=4, base_lines=40, new_lines=417)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `sing-box/ip/ai.json` (ratio=0.9221, changed=379, add=378, del=1, base_lines=34, new_lines=411)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1606, changed=4046, add=3143, del=903, base_lines=1246, new_lines=3486)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.5185, changed=14, add=12, del=2, base_lines=17, new_lines=27)

<!-- END_GUARD_REPORT -->
