import collections


class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        domain_counts = collections.defaultdict(int)
        for cpdomain in cpdomains:
            times, domains = cpdomain.split()
            print("times", times)
            print("domains", domains)
            times = int(times)
            domain_counts[domains] += times
            print(domain_counts)
            while '.' in domains:
                domains = domains[domains.index('.') + 1:]
                domain_counts[domains] += times
                # 各种骚气的操作啊
        return [str(v) + ' ' + d for d, v in domain_counts.items()]


if __name__ == '__main__':
    list = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(list)
    print(Solution().subdomainVisits(list))
