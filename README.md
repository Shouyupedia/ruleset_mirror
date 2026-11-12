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

- Updated from: `f41b950f8e6e148dd9025882e94be253350f2e62`
- Upstream head: `1daa7ce11dd872759ef7a69f2eed6b50bff38382`
- Time (UTC): 2026-11-12 19:56:34Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 23
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 13

### Skipped file list
- `Clash/ip/ai.txt` (ratio=0.9406, changed=523, add=519, del=4, base_lines=41, new_lines=556)
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1776, changed=4058, add=3126, del=932, base_lines=1252, new_lines=3446)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `LegacyClashPremium/ip/ai.txt` (ratio=0.9423, changed=523, add=519, del=4, base_lines=40, new_lines=555)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `List/ip/ai.conf` (ratio=0.9406, changed=523, add=519, del=4, base_lines=41, new_lines=556)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1773, changed=4058, add=3126, del=932, base_lines=1253, new_lines=3447)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `Surfboard/ip/ai.conf` (ratio=0.9423, changed=523, add=519, del=4, base_lines=40, new_lines=555)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `sing-box/ip/ai.json` (ratio=0.9417, changed=517, add=516, del=1, base_lines=34, new_lines=549)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1785, changed=4054, add=3124, del=930, base_lines=1246, new_lines=3440)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.5185, changed=14, add=12, del=2, base_lines=17, new_lines=27)

<!-- END_GUARD_REPORT -->
