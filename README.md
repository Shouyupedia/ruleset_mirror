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

- Updated from: `3d2cf86cac41f2c66f99e752986116170dc73a0a`
- Upstream head: `07d4fbb4b0dab309a2a5beb4f22557d4cf742e67`
- Time (UTC): 2026-10-27 22:16:07Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 13

### Skipped file list
- `Clash/ip/ai.txt` (ratio=0.9167, changed=363, add=359, del=4, base_lines=41, new_lines=396)
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1696, changed=4110, add=3186, del=924, base_lines=1252, new_lines=3514)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `LegacyClashPremium/ip/ai.txt` (ratio=0.9190, changed=363, add=359, del=4, base_lines=40, new_lines=395)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `List/ip/ai.conf` (ratio=0.9167, changed=363, add=359, del=4, base_lines=41, new_lines=396)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1693, changed=4110, add=3186, del=924, base_lines=1253, new_lines=3515)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `Surfboard/ip/ai.conf` (ratio=0.9190, changed=363, add=359, del=4, base_lines=40, new_lines=395)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `sing-box/ip/ai.json` (ratio=0.9177, changed=357, add=356, del=1, base_lines=34, new_lines=389)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1705, changed=4106, add=3184, del=922, base_lines=1246, new_lines=3508)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.5185, changed=14, add=12, del=2, base_lines=17, new_lines=27)

<!-- END_GUARD_REPORT -->
