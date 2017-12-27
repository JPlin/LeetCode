# IP to CIDR

class Solution:
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        ipInt = self.ipToInt(ip)
        ans = []
        x = 0
        while x < n:
            zeros = self.countZeros( ipInt + x)
            while x + ( 1 << zeros) > n:
                zeros -= 1
            ans.append(self.intToIp(ipInt + x) + "/" + str(32 - zeros))
            x += 1 << zeros
        return ans

    def ipToInt(self , ip):
        ans = 0
        for idx , part in enumerate(ip.split('.')[::-1]):
            ans += int(part) << idx*8
        return ans

    def intToIp(self , ipInt):
        ans = []
        for x in range(4):
            ans.append((ipInt >> x * 8) & 255)
        return '.'.join(list(map(str , ans[::-1])))

    def countZeros(self , ip):
        cnt = 0
        while ip:
            if ip & 1 : break
            cnt += 1
            ip >>= 1
        return cnt

if __name__ == '__main__':
    solution = Solution()
    print(solution.ipToCIDR('255.0.0.7' , 10))