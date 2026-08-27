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

- Updated from: `dba65eaee31080aa63b89381cd5a4d3865cecacc`
- Upstream head: `f9b5bdefef2e5bfb72c8bd8b63754567654889fc`
- Time (UTC): 2026-08-27 22:17:08Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1567, changed=3986, add=3090, del=896, base_lines=1252, new_lines=3446)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1564, changed=3986, add=3090, del=896, base_lines=1253, new_lines=3447)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1570, changed=3980, add=3087, del=893, base_lines=1246, new_lines=3440)

<!-- END_GUARD_REPORT -->
