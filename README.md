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

- Updated from: `eef7e91c2fdabcd9a6237e125520cc11dd864f94`
- Upstream head: `59ac1b2efe60e175e4809fb59839c16b26d7a40e`
- Time (UTC): 2026-10-27 12:15:38Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 15
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 13

### Skipped file list
- `Clash/ip/ai.txt` (ratio=0.8036, changed=135, add=131, del=4, base_lines=41, new_lines=168)
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1696, changed=4110, add=3186, del=924, base_lines=1252, new_lines=3514)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `LegacyClashPremium/ip/ai.txt` (ratio=0.8084, changed=135, add=131, del=4, base_lines=40, new_lines=167)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `List/ip/ai.conf` (ratio=0.8036, changed=135, add=131, del=4, base_lines=41, new_lines=168)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1693, changed=4110, add=3186, del=924, base_lines=1253, new_lines=3515)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5294, changed=18, add=15, del=3, base_lines=22, new_lines=34)
- `Surfboard/ip/ai.conf` (ratio=0.8084, changed=135, add=131, del=4, base_lines=40, new_lines=167)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5455, changed=18, add=15, del=3, base_lines=21, new_lines=33)
- `sing-box/ip/ai.json` (ratio=0.8012, changed=129, add=128, del=1, base_lines=34, new_lines=161)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1705, changed=4106, add=3184, del=922, base_lines=1246, new_lines=3508)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.5185, changed=14, add=12, del=2, base_lines=17, new_lines=27)

<!-- END_GUARD_REPORT -->
